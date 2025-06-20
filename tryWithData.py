obj1=[
    {
        "filename": "1st filepoll",
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
    },
    {
        "filename": "GoogleCloudPlatformAudit Logs_ccp/data_connector_poller.json",
        "content": [
            {
                "type": "Microsoft.SecurityInsights/dataConnectors",
                "apiVersion": "2022-10-01-preview",
                "name": "{{workspace}}/Microsoft.SecurityInsights/GCPAuditLogs",
                "kind": "GCP",
                "properties": {
                    "connectorDefinitionName": "GCPAuditLogsDefinition",
                    "dataType": "GCPAuditLogs",
                    "dcrConfig": {
                        "streamName": "SENTINEL_GCP_AUDIT_LOGS"
                    },
                    "auth": {
                        "serviceAccountEmail": "{{GCPServiceAccountEmail}}",
                        "projectNumber": "{{GCPProjectNumber}}",
                        "workloadIdentityProviderId": "{{GCPWorkloadIdentityProviderId}}"
                    },
                    "request": {
                        "projectId": "{{GCPProjectId}}",
                        "subscriptionNames": [
                            "{{GCPSubscriptionName}}"
                        ]
                    }
                }
            }
        ]
    },
    {
        "filename": "file2_JiraAudit_Polling",
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
                    "UserName": "{{userid}}"
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
    },
        {
        "filename": "file3_JiraAudit_Polling",
        "content": {
            "name": "AtlassianJiraCCPPolling",
            "apiVersion": "2022-12-01-preview",
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
    }    ,{
        "filename": "file4poller.json",
        "content": [
            {
                "type": "Microsoft.SecurityInsights/dataConnectors",
                "apiVersion": "2022-10-01-preview",
                "name": "{{workspace}}/Microsoft.SecurityInsights/GCPAuditLogs",
                "kind": "GCP",
                "properties": {
                    "connectorDefinitionName": "GCPAuditLogsDefinition",
                    "dataType": "GCPAuditLogs",
                    "dcrConfig": {
                        "streamName": "SENTINEL_GCP_AUDIT_LOGS"
                    },
                    "request": {
                        "projectId": "{{GCPProjectId}}",
                        "subscriptionNames": [
                            "{{GCPSubscriptionName}}"
                        ]
                    }
                }
            }
        ]
    }





]










# dict has these certain keys
# value is a set 
# "valueConditions" is a dict
# elements is a dict 

auth_elements={
    "type":{ "valueConditions":{"APIKey":{"elements":{"ApiKey":{},"ApiKeyName":{},"ApiKeyIdentifier":{}}},
                                "Basic":{"elements":{"UserName":{}, "Password":{}}},
                                "OAuth2":{"elements":{"ClientId":{},
                                                      "ClientSecret":{},
                                                      "GrantType":{ "valueConditions":{ 
                                                                                "authorization_code":{"elements": {"Scope":{},"RedirectUri":{},"AuthorizationCode":{}}}}
                                                                                },
                                                      "TokenEndpoint":{},
                                                      "AuthorizationEndpoint":{}}},
                                "JwtToken":{"elements":{"username": { "elements":{"key":{},"value":{}}},
                                                        "password": { "elements":{"key":{},"value":{}}},
                                                        "IsJsonRequest": {},
                                                        "TokenEndpoint":{} }}}
            }
    }

checks_RestApiPoller= {"elements":{
    "name":{},
    "properties":{
        "elements":{ "auth":{ "elements":auth_elements},
                    "request":{"elements":{"apiEndpoint":{}}},
                    "response":{ "elements":{"EventsJsonPaths":{}}},
                    "dcrConfig":{ "elements":{"dataCollectionEndpoint":{},"dataCollectionRuleImmutabled":{},"StreamName":{}}}}
    }
}}


allowedKindvalueConditions = {
    "RestApiPoller": checks_RestApiPoller,
    "GCP": {},
    "AmazonWebServicesS3": {},
    "AmazonWebServicesCloudTrail": {},
    "AzureActiveDirectory": {},
    "MicrosoftCloudAppSecurity": {},
    "Office365": {},
    "Office365Project": {},
    "OfficePowerBI": {},
    "PurviewAudit": {},
    "Office365CommunicationsCompliance": {},
    "ThreatIntelligence": {},
    "AzureAdvancedThreatProtection": {},
    "AzureSecurityCenter": {},
    "MicrosoftDefenderAdvancedThreatProtection": {},
    "MicrosoftThreatProtection": {},
    "ThreatIntelligenceTaxii": {},
    "ThreatIntelligenceTaxiiExport": {},
    "OfficeATP": {},
    "OfficeIRM": {},
    "MicrosoftPurviewInformationProtection": {},
    "Dynamics365": {},
    "MicrosoftThreatIntelligence": {},
    "PremiumMicrosoftDefenderForThreatIntelligence": {},
    "APIPolling": {},
    "GenericUI": {},
    "StaticUI": {},
    "IOT": {},
    "AAD": {},
    "ASC": {},
    "MCAS": {},
    "WebSocket": {},
    "ThreatVulnerabilityManagement": {},
    "StorageAccountBlobContainer": {},
    "Push": {},
    "OCI": {}
}



checks_polling={
     "elements":{
        "type": { "value":{"Microsoft.SecurityInsights/dataConnectors"}},
        "kind": {"valueConditions":allowedKindvalueConditions}
    }
}


# dict has these certain keys
# value is a set 
# "valueConditions" is a dict
# elements is a dict 

# Recursive validation functions

def valuereader(rule, value, path, errors):
    if "value" in rule:
        if value not in rule["value"]:
            errors.append(f"{path}: Value '{value}' not in allowed set {rule['value']}")

def valueConditionsreader(rule, value, value_data, path, errors):
    if "valueConditions" in rule:
        if value in rule["valueConditions"]:
            elementreder(rule["valueConditions"][value], value_data, f"{path}", errors)

def elementreder(rule, data, path, errors):
    if "elements" in rule:
        for key, subrule in rule["elements"].items():
            if isinstance(data, dict) and key in data:
                elementreder(subrule, data[key], f"{path}.{key}", errors)
            else:
                errors.append(f"{path}: Missing required key '{key}'")
    valuereader(rule, data, path, errors)
    valueConditionsreader(rule, data, data, path, errors)


validation_errors = []
errorMessage =""
flag=True
for item in obj1:
    filename = item["filename"]
    if "poll" in filename.lower():
        content = item["content"]
        if isinstance(content, list):
            content = content[0]
        errors = []
        elementreder(checks_polling, content, "root", errors)
        if errors:
            print(flag)
            validation_errors.append(f"{filename} -\n" + "\n".join(errors))
            flag=False

for i in validation_errors:
    errorMessage= errorMessage+"\n \n \n"+i

print(errorMessage)




                 
                 
            
            