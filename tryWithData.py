data=[
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
                    "UserName": "Hi",
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
from validator import validate_with_rules


overall_flag = True
messages = []

for entry in data:
    title = entry.get("filename", "<unknown>")
    content = entry["content"][0] if isinstance(entry.get("content"), list) else entry.get("content", {})

    valid, errs = validate_with_rules(content)
    if not valid:
        overall_flag = False
        messages.append(f"— {title}:\n{errs}")

if overall_flag:
    #return JSONResponse(status_code=200, content={"status": "passed", "message": "All validation tests passed"})
    print("passed")
else:
    '''return JSONResponse(
        status_code=400,
        content={
            "status": "failed",
            "message": "\n\n".join(messages)
        }
    )'''
    print("\n\n".join(messages))

