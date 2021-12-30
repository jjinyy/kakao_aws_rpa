import json
import base64
import requests
import urllib.request
import urllib3
import ssl
#from . import test1
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()

#Token 받아오기
def getToken(url,tenancyName,userName,password,verify):
    url = "https://154.10.6.152"
    data = {
        "tenancyName": tenancyName,
        "usernameOrEmailAddress": userName,
        "password": password
    }
    sess = requests.Session()
    req = requests.post(url+"/api/Account/Authenticate",data,verify=False)
    if(req.status_code == 200):
        resJson = req.json()
        return resJson["result"]
    else:
        return None

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