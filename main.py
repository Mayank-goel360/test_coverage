from fastapi import FastAPI, HTTPException, Request
import uvicorn
import json
from fastapi.responses import JSONResponse
from logger import get_logger

app= FastAPI()
logger=get_logger(__name__)

@app.get("/")
def getResponse():
    return {"message":"Validation API is live"}





@app.post("/")
async def validatonCheck(request:Request):

    data = await request.json()  
    try:
        if not data:
            return JSONResponse(status_code=400, content={
                "status": "failed",
                "message": "No data provided"
            })



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


        validation_errors = []
        errorMessage =""
        flag=True
        for item in data:
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



        logger.info(f"Validation result: flag={flag}, errorMessage={errorMessage}")

        if(flag):
            return JSONResponse(status_code=200, content={
            "status": "passed",
            "message":  "All validation tests passed"
        })
        else:
            return JSONResponse(status_code=400, content={
            "status": "failed",
            "message": errorMessage
        })

    except Exception as e:
        
        logger.error(f"Exception occurred in validation check", exc_info=True)
        return JSONResponse(status_code=500, content={
            "status": "failed",
            "message": "Internal server error "
        })



if __name__=="__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
