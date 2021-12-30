import json
import base64
import requests
import urllib.request
import urllib3
import ssl
from getOr import getToken
from getOr import getToOr
from getOr import postToOr
from returnKakaoForm import dataForm
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()
  
#Main     
def lambda_handler(event, context): 
    baseUrl = "https://154.10.6.152"
    orUrl = {
        'Robots':baseUrl+"/odata/Robots",
        "Jobs":baseUrl+"/odata/Jobs",
        "Processes":baseUrl+"/odata/Processes",
        "Releases":baseUrl+"/odata/Releases",
        "StartJobs": baseUrl+"/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
    }
    
    ####################################################################################
    #Token 가져오기
    key = getToken(baseUrl,"default","jjjiny","hb1060at^^^",verify=False)

    ####################################################################################
    #카카오 데이터 가져오기
    #input parameter가 있는 경우
    #InputData = {"sendMsgUser":event["action"]["params"]["sendMsgUser"],"sendMsgTxt":event["action"]["params"]["sendMsgTxt"]}
    #return format(InputData)
    
    #Or에 맞는 형식으로 변환
    data = {
        "startInfo": {
            "ReleaseKey": "698e7712-66ec-4ee7-9cfc-37234dac6087",
            "Strategy": "Specific",
            "RobotIds": [8],
            "NoOfRobots": 0,
            "JobsCount": 0,
            "Source": "Manual",
            #"InputArguments": format(InputData)
        }
    }
    
    #job 실행
    res = postToOr(orUrl["StartJobs"],key,data,verify=False)
    return dataForm("monitoring",None)
    # print(res)
    # if (res != None):
    #     print("success")
    #     return dataForm("startJobMsg","ResponseTalk")
    #return {"body":res}

    #################################################################################
    # # 실행된 작업의 key 저장
    # #jobkey = res["Key"]
    
    # #작업상태(필터걸어서 특정작업의 상태만 출력하게
    # #사용자-작업으로 매핑시켜야 할 듯... 방안고민필요
    # req = getToOr(orUrl["Jobs"] + "?$filter=Key eq ee07df58-de0d-449c-9865-cf3759f42ec6",key,verify=False) # + "?$filter=Key eq "+be43281e-95a4-4e81-9d56-037bb1ea7ed0
    # print(req)
