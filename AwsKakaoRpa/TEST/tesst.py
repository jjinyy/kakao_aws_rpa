import json
import base64
import requests
import urllib.request
import urllib3
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()


def getAuthKey(url,tenancyName,userName,password,verify):
    api_url = "https://154.10.6.152"
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

def postUiPathAPI(url,key,data,verify):
    api_url = "https://154.10.6.152"
    head = {
        "Content-Type" : "application/json",
        "X-UIPATH-OrganizationUnitId":"1",
        "Authorization" : "Bearer " + key
    }
    
    req = requests.post(url,json.dumps(data),headers=head,verify=False)

    if(req.status_code == 200 or req.status_code == 201):
        return req.json()
        #print(req["value"][0]["State"])
        #return{
        #    req["value"][0]["State"]
        #}
       
  
    else:
        return None

def getUiPathAPI(url,key,verify):
    api_url = "https://154.10.6.152"
    head = {
        "Content-Type" : "application/json",
        "X-UIPATH-OrganizationUnitId":"1",
        "Authorization" : "Bearer " + key
    }
    
    req = requests.get(url,headers=head,verify=False)
    if(req.status_code == 200):
        return req.json()
    else:
        return None

def lambda_handler(event, context): 
    my_endpoint = "https://154.10.6.152"
    api_url = {
        'Robots':my_endpoint+"/odata/Robots",
        "Jobs":my_endpoint+"/odata/Jobs",
        "Processes":my_endpoint+"/odata/Processes",
        "Releases":my_endpoint+"/odata/Releases"
    }
    key = getAuthKey(my_endpoint,"default","jjjiny","hb1060at^^^",verify=False)
    res = getUiPathAPI(api_url["Releases"],key,verify=False)


## Job 실행
    api_url = "https://154.10.6.152"
    key = getAuthKey(my_endpoint,"default","jjjiny","hb1060at^^^",verify=False)
    
    head = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + key
    }

    print("********** Robots Info")
    req = requests.post(api_url+"/odata/Robots",headers=head,verify=False)
    if(req.status_code == 200):
        req.json()
    else:
        print(req)

    print("********** Jobs Info")
    req = requests.get(api_url+"/odata/Jobs",headers=head,verify=False)
    if(req.status_code == 200):
        req.json()
    else:
        print(req)