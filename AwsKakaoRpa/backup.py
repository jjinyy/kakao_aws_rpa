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

# #Token 받아오기
# def getToken(url,tenancyName,userName,password,verify):
#     data = {
#         "tenancyName": tenancyName,
#         "usernameOrEmailAddress": userName,
#         "password": password
#     }
#     sess = requests.Session()
#     req = requests.post(url+"/api/Account/Authenticate",data,verify=False)
#     if(req.status_code == 200):
#         resJson = req.json()
#         return resJson["result"]
#     else:
#         return None

#Post
def postToOr(url,key,data,verify):
    headers = {
        "Content-Type" : "application/json",
        "X-UIPATH-OrganizationUnitId":"1",
        "Authorization" : "Bearer " + key
    }
    req = requests.post(url,json.dumps(data),headers=headers,verify=False)
    if(req.status_code == 200 or req.status_code == 201):
        #returnData = {"version": "2.0","template":{"outputs":[{"simpleText": {"text": "작업이 실행되었습니다."}}]}}
        return req.json()
        #return returnData
    else:
        return None

#Get
def getToOr(url,key,verify):
    headers = {
        "Content-Type" : "application/json",
        "X-UIPATH-OrganizationUnitId":"1",
        "Authorization" : "Bearer " + key
    }
    req = requests.get(url,headers=headers,verify=False)
    if(req.status_code == 200):
        return req.json()
    else:
        return None
  
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
    
    ###################################################################################
    #작업목록 및 releases key
    res = getToOr(orUrl["Releases"],key,verify=False)
    try :
        for i in range(0,100):
            #print(res)
            print(res["value"][i]["ProcessKey"] + " / " + res["value"][i]["Key"])
    except Exception:
        print("finish")
    
    # ####################################################################################
    # #카카오 데이터 가져오기
    # #input parameter가 있는 경우
    # InputData = {"ID":event["action"]["params"]["ID"],"PW":event["action"]["params"]["PW"]}
    # #return format(InputData)
    # #Or에 맞는 형식으로 변환
    # data = {
    #     "startInfo": {
    #         "ReleaseKey": "be43281e-95a4-4e81-9d56-037bb1ea7ed0",
    #         "Strategy": "Specific",
    #         "RobotIds": [8],
    #         "NoOfRobots": 0,
    #         "JobsCount": 0,
    #         "Source": "Manual",
    #         "InputArguments": format(InputData)
    #     }
    # }
    
    # #job 실행
    # res = postToOr(orUrl["StartJobs"],key,data,verify=False)
    # if (res != None):
    #     print("success")
    #     #return {"version": "2.0","template":{"outputs":[{"simpleText": {"text": "작업이 실행되었습니다."}}]}}
    #     #print(data)
    #     return dataForm("bottonListMsg")
    # #return {"body":res}

    # #################################################################################
    # # # 실행된 작업의 key 저장
    # # #jobkey = res["Key"]
    
    # # #작업상태(필터걸어서 특정작업의 상태만 출력하게
    # # #사용자-작업으로 매핑시켜야 할 듯... 방안고민필요
    # # req = getToOr(orUrl["Jobs"] + "?$filter=Key eq ee07df58-de0d-449c-9865-cf3759f42ec6",key,verify=False) # + "?$filter=Key eq "+be43281e-95a4-4e81-9d56-037bb1ea7ed0
    # # print(req)
