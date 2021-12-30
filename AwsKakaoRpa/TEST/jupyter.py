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
## Robot Info, Job Info등
## Job 실행
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
    my_endpoint = "https://154.10.6.152"

    key = getAuthKey(my_endpoint,"default","jjjiny","hb1060at^^^",verify=False)
    # print(reqResult)
    
    #return{
    #    'body':json.dumps(event["action"]["params"]["ID"])
    #}
    
    #InputData={'ID':json.dumps(event["action"]["params"]["ID"]),'PW':json.dumps(event["action"]["params"]["PW"])}
    
    #print(InputData)
    
    #ID = json.loads(event["action"]["params"]["ID"])
    #PW = json.loads(event["action"]["params"]["PW"]) # request body 받음
    
    InputData = {"ID":event["action"]["params"]["ID"],"PW":event["action"]["params"]["PW"]}
    
    #return format(InputData)
    
    data = {
        "startInfo": {
            "ReleaseKey": "be43281e-95a4-4e81-9d56-037bb1ea7ed0",
            "Strategy": "All",
            #"RobotIds": [8],
            "NoOfRobots": 0,
            "JobsCount": 0,
            "Source": "Manual",
            "InputArguments": format(InputData)
        }
    }
    res = postUiPathAPI(my_endpoint+"/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs",key,data,verify=False)
    
    test = json.dumps(res)
        
    
    dicres = json.loads(test)["value"][0]["State"]
    
    return{
        #'State':dicres["value"][0]["State"]
        "body":json.dumps(dicres)
    }
  
    
    #return{
    #        'value':json.dumps(dicres)["value"]
    #}
    
    #print(res)


    #api_url = "https://154.10.6.152"
    #data = {
    #    "tenancyName": "default",
    #    "usernameOrEmailAddress": "jjjiny",
    #    "password": "hb1060at^^^"
    #}
    #sess = requests.Session()
    #req = requests.post(api_url+"/api/Account/Authenticate",data,verify=False)
    #resJson = req.json()

    #reqResult = resJson["result"]
    #print(reqResult)
    
    #return{
    #        'body':json.dumps(resJson1)['state']
    #}