import json

# Sample data (obj1) and rule definitions
obj1 = [
    {
        "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
        "content": {
            "name": "AtlassianJiraCCPPolling",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors_wrong",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "connectorDefinitionName": "JiraAuditCCPDefinition",
                "dataType": "Jira_Audit_v2_CL",
                "dcrConfig": {
                    "dataCollectionEndpoint": "{{dataCollectionEndpoint}}",
                    "dataCollectionRuleImmutableId": "{{dataCollectionRuleImmutableId}}",
                    "streamName": "Custom-Jira_Audit_v2_CL"
                },
                "auth": {
                    "type": "Basic",
                    "UserName": "{{userid}}",
                    "Password": "{{apikey}}"
                },
                "request": {
                    "apiEndpoint": "https://{{jiraorganizationurl}}/rest/api/3/auditing/record",
                    "httpMethod": "GET",
                    "retryCount": 3,
                    "timeoutInSeconds": 60,
                    "queryTimeFormat": "yyyy-MM-ddTHH:mm:ssZ",
                    "headers": {
                        "Accept": "application/json",
                        "User-Agent": "Scuba"
                    },
                    "startTimeAttributeName": "from",
                    "endTimeAttributeName": "to"
                },
                "paging": {
                    "pagingType": "Offset",
                    "offsetParaName": "offset",
                    "pageSizeParaName": "limit",
                    "pageSize": 1000
                },
                "response": {
                    "eventsJsonPaths": [
                        "$.records"
                    ],
                    "format": "json"
                }
            }
        }
    }
]

# Rule definitions
auth_elements = {
    "type": {
        "valueConditions": {
            "APIKey": {"elements": {"ApiKey": {}, "ApiKeyName": {}, "ApiKeyIdentifier": {}}},
            "Basic": {"elements": {"UserName": {}, "Password": {}}},
            "OAuth2": {
                "elements": {
                    "ClientId": {},
                    "ClientSecret": {},
                    "GrantType": {
                        "valueConditions": {
                            "authorization_code": {
                                "elements": {"Scope": {}, "RedirectUri": {}, "AuthorizationCode": {}}
                            }
                        }
                    },
                    "TokenEndpoint": {},
                    "AuthorizationEndpoint": {}
                }
            },
            "JwtToken": {
                "elements": {
                    "username": {"elements": {"key": {}, "value": {}}},
                    "password": {"elements": {"key": {}, "value": {}}},
                    "IsJsonRequest": {},
                    "TokenEndpoint": {}
                }
            }
        }
    }
}

checks_RestApiPoller = {
    "elements": {
        "name": {},
        "properties": {
            "elements": {
                "auth": {"elements": auth_elements},
                "request": {"elements": {"apiEndpoint": {}}},
                "response": {"elements": {"EventsJsonPaths": {}}},
                "dcrConfig": {
                    "elements": {
                        "dataCollectionEndpoint": {},
                        "dataCollectionRuleImmutabled": {},
                        "StreamName": {}
                    }
                }
            }
        }
    }
}

allowedKindvalueConditions = {
    "RestApiPoller": checks_RestApiPoller,
    "GCP": {}, "AmazonWebServicesS3": {}, "AmazonWebServicesCloudTrail": {},
    "AzureActiveDirectory": {}, "MicrosoftCloudAppSecurity": {}, "Office365": {},
    "Office365Project": {}, "OfficePowerBI": {}, "PurviewAudit": {},
    "Office365CommunicationsCompliance": {}, "ThreatIntelligence": {},
    "AzureAdvancedThreatProtection": {}, "AzureSecurityCenter": {},
    "MicrosoftDefenderAdvancedThreatProtection": {}, "MicrosoftThreatProtection": {},
    "ThreatIntelligenceTaxii": {}, "ThreatIntelligenceTaxiiExport": {},
    "OfficeATP": {}, "OfficeIRM": {}, "MicrosoftPurviewInformationProtection": {},
    "Dynamics365": {}, "MicrosoftThreatIntelligence": {},
    "PremiumMicrosoftDefenderForThreatIntelligence": {}, "APIPolling": {},
    "GenericUI": {}, "StaticUI": {}, "IOT": {}, "AAD": {}, "ASC": {},
    "MCAS": {}, "WebSocket": {}, "ThreatVulnerabilityManagement": {},
    "StorageAccountBlobContainer": {}, "Push": {}, "OCI": {}
}

checks_polling = {
    "elements": {
        "type": {"value": {"Microsoft.SecurityInsights/dataConnectors"}},
        "kind": {"valueConditions": allowedKindvalueConditions}
    }
}

# Recursive validation functions
def valuereader(rule, value, path, errors):
    if "value" in rule:
        if value not in rule["value"]:
            errors.append(f"{path}: Value '{value}' not in allowed set {rule['value']}")

def valueConditionsreader(rule, value, value_data, path, errors):
    if "valueConditions" in rule:
        if value in rule["valueConditions"]:
            elementreder(rule["valueConditions"][value], value_data, f"{path}.{value}", errors)

def elementreder(rule, data, path, errors):
    if "elements" in rule:
        for key, subrule in rule["elements"].items():
            if isinstance(data, dict) and key in data:
                elementreder(subrule, data[key], f"{path}.{key}", errors)
            else:
                errors.append(f"{path}: Missing required key '{key}'")
    valuereader(rule, data, path, errors)
    valueConditionsreader(rule, data, data, path, errors)

# Run validation
validation_errors = []
for item in obj1:
    filename = item["filename"]
    if "poll" in filename.lower():
        content = item["content"]
        if isinstance(content, list):
            content = content[0]
        errors = []
        elementreder(checks_polling, content, "", errors)
        if errors:
            validation_errors.append(f"{filename} -\n" + "\n".join(errors))

# Save results to a file
print(validation_errors[0])


