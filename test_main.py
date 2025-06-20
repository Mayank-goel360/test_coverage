# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# def test_validation_pass():
#     payload = [{
#         "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
#         "content":
# {
#     "name": "AtlassianJiraCCPPolling",
#     "apiVersion": "2022-12-01-preview",
#     "type": "Microsoft.SecurityInsights/dataConnectors",
#     "location": "{{location}}",
#     "kind": "RestApiPoller",
#     "properties": {
#         "connectorDefinitionName": "JiraAuditCCPDefinition",
#         "dataType": "Jira_Audit_v2_CL",
#         "dcrConfig": {
#             "dataCollectionEndpoint": "{{dataCollectionEndpoint}}",
#             "dataCollectionRuleImmutableId": "{{dataCollectionRuleImmutableId}}",
#             "streamName": "Custom-Jira_Audit_v2_CL"
#         },
#         "auth": {
#             "type": "Basic",
#             "UserName": "{{userid}}",
#             "Password": "{{apikey}}"
#         },
#         "request": {
#             "apiEndpoint": "https://{{jiraorganizationurl}}/rest/api/3/auditing/record",
#             "httpMethod": "GET",
#             "retryCount": 3,
#             "timeoutInSeconds": 60,
#             "queryTimeFormat": "yyyy-MM-ddTHH:mm:ssZ",
#             "headers": {
#                 "Accept": "application/json",
#                 "User-Agent": "Scuba"
#             },
#             "startTimeAttributeName": "from",
#             "endTimeAttributeName": "to"
#         },
#         "paging": {
#             "pagingType": "Offset",
#             "offsetParaName": "offset",
#             "pageSizeParaName": "limit",
#             "pageSize": 1000
#         },
#         "response": {
#             "eventsJsonPaths": [
#                 "$.records"
#             ],
#             "format": "json"
#         }
#     }
# }}
#     ]

#     response = client.post("/", json=payload)
#     assert response.status_code == 200
#     assert response.json()["status"] == "passed"

# def test_validation_fail_missing_type():
#     payload = [
#     {
#         "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
#         "content": {
#             "name": "AtlassianJiraCCPPolling",
#             "apiVersion": "2022-12-01-preview",
#             "type": "Microsoft.SecurityInsights/dataConnectors_wrong",
#             "location": "{{location}}",
#             "kind": "RestApiPoller",
#             "properties": {
#                 "connectorDefinitionName": "JiraAuditCCPDefinition",
#                 "dataType": "Jira_Audit_v2_CL",
#                 "dcrConfig": {
#                     "dataCollectionEndpoint": "{{dataCollectionEndpoint}}",
#                     "dataCollectionRuleImmutableId": "{{dataCollectionRuleImmutableId}}",
#                     "streamName": "Custom-Jira_Audit_v2_CL"
#                 },
#                 "auth": {
#                     "type": "Basic",
#                     "UserName": "{{userid}}",
#                     "Password": "{{apikey}}"
#                 },
#                 "request": {
#                     "apiEndpoint": "https://{{jiraorganizationurl}}/rest/api/3/auditing/record",
#                     "httpMethod": "GET",
#                     "retryCount": 3,
#                     "timeoutInSeconds": 60,
#                     "queryTimeFormat": "yyyy-MM-ddTHH:mm:ssZ",
#                     "headers": {
#                         "Accept": "application/json",
#                         "User-Agent": "Scuba"
#                     },
#                     "startTimeAttributeName": "from",
#                     "endTimeAttributeName": "to"
#                 },
#                 "paging": {
#                     "pagingType": "Offset",
#                     "offsetParaName": "offset",
#                     "pageSizeParaName": "limit",
#                     "pageSize": 1000
#                 },
#                 "response": {
#                     "eventsJsonPaths": [
#                         "$.records"
#                     ],
#                     "format": "json"
#                 }
#             }
#         }
#     }
#     ]

#     response = client.post("/", json=payload)
#     assert response.status_code == 400
#     assert response.json()["status"] == "failed"
#     assert "type" in response.json()["message"]



from fastapi.testclient import TestClient
from main import app

client = TestClient(app)



def test_validation_pass():
    payload = [{
        "filename": "AtlassianJiraAudit_ccpv2/JiraAudit_PollingConfig.json",
        "content":
{
    "name": "AtlassianJiraCCPPolling",
    "apiVersion": "2022-12-01-preview",
    "type": "Microsoft.SecurityInsights/dataConnectors",
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

    response = client.post("/", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "passed"

def test_validation_fail_missing_type():
    payload = [
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

    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"
    assert "type" in response.json()["message"]


def test_valid_basic_auth():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "eastus",
            "kind": "RestApiPoller",
            "properties": {
                "connectorDefinitionName": "TestDefinition",
                "dataType": "Test_CL",
                "dcrConfig": {
                    "dataCollectionEndpoint": "endpoint",
                    "dataCollectionRuleImmutableId": "ruleId",
                    "streamName": "stream"
                },
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                },
                "request": {
                    "apiEndpoint": "https://example.com",
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
                    "eventsJsonPaths": ["$.records"],
                    "format": "json"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "passed"

def test_missing_type():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "location": "eastus",
            "kind": "RestApiPoller",
            "properties": {}
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_invalid_type():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "type": "Invalid.Type",
            "location": "eastus",
            "kind": "RestApiPoller",
            "properties": {}
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_missing_kind():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "eastus",
            "properties": {}
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_missing_auth():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "eastus",
            "kind": "RestApiPoller",
            "properties": {}
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_missing_request():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "eastus",
            "kind": "RestApiPoller",
            "properties": {
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_missing_response():
    payload = [{
        "filename": "polling_config.json",
        "content": {
            "name": "TestConnector",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "eastus",
            "kind": "RestApiPoller",
            "properties": {
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                },
                "request": {
                    "apiEndpoint": "https://example.com",
                    "httpMethod": "GET"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_empty_payload():
    payload = []
    response = client.post("/", json=payload)
    assert response.status_code == 400
    assert response.json()["status"] == "failed"

def test_non_poll_filename():
    payload = [{
        "filename": "config.json",
        "content": {
            "type": "Microsoft.SecurityInsights/dataConnectors"
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "passed"


# Test 10: Missing 'auth' block
def test_missing_auth_block():
    payload = [{
        "filename": "TestPoller/PollingConfig.json",
        "content": {
            "name": "TestPoller",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "request": {},
                "response": {
                    "eventsJsonPaths": ["$.records"],
                    "format": "json"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400


# Test 11: Missing 'request' block
def test_missing_request_block():
    payload = [{
        "filename": "TestPoller/PollingConfig.json",
        "content": {
            "name": "TestPoller",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                },
                "response": {
                    "eventsJsonPaths": ["$.records"],
                    "format": "json"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400
    

# Test 12: Missing 'response' block
def test_missing_response_block():
    payload = [{
        "filename": "TestPoller/PollingConfig.json",
        "content": {
            "name": "TestPoller",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                },
                "request": {
                    "apiEndpoint": "https://example.com",
                    "httpMethod": "GET"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400

# Test 13: Incorrect 'kind' value
def test_incorrect_kind_value():
    payload = [{
        "filename": "TestPoller/PollingConfig.json",
        "content": {
            "name": "TestPoller",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "{{location}}",
            "kind": "UnknownKind",
            "properties": {
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                },
                "request": {
                    "apiEndpoint": "https://example.com",
                    "httpMethod": "GET"
                },
                "response": {
                    "eventsJsonPaths": ["$.records"],
                    "format": "json"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code == 400


# Test 14: Missing 'dcrConfig' block
def test_missing_dcr_config():
    payload = [{
        "filename": "TestPoller/PollingConfig.json",
        "content": {
            "name": "TestPoller",
            "apiVersion": "2022-12-01-preview",
            "type": "Microsoft.SecurityInsights/dataConnectors",
            "location": "{{location}}",
            "kind": "RestApiPoller",
            "properties": {
                "auth": {
                    "type": "Basic",
                    "UserName": "user",
                    "Password": "pass"
                },
                "request": {
                    "apiEndpoint": "https://example.com",
                    "httpMethod": "GET"
                },
                "response": {
                    "eventsJsonPaths": ["$.records"],
                    "format": "json"
                }
            }
        }
    }]
    response = client.post("/", json=payload)
    assert response.status_code in [200, 400]



