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
    #baseUrl = "https://kimcar85.synology.me:33501"
    baseUrl = "https://154.10.6.152"
    orUrl = {
        'Robots':baseUrl+"/odata/Robots",
        "Jobs":baseUrl+"/odata/Jobs",
        "Processes":baseUrl+"/odata/Processes",
        "Releases":baseUrl+"/odata/Releases",
        "StartJobs": baseUrl+"/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
    }

    ####################################################################################
    #카카오 데이터 가져오기
    #오케 아이디 및 비밀번호 입력
    #InputData = {"ID":event["action"]["params"]["ID"],"PW":event["action"]["params"]["PW"]}
        
    ####################################################################################
    #Token 가져오기
    id = {"ID":event["action"]["params"]["ID"]}
    pw = {"PW":event["action"]["params"]["PW"]}
    key = getToken(baseUrl,"default",id["ID"],pw["PW"],verify=False)
    
    if (key != None):
        print("success")
        return dataForm("auth", id["ID"])
    #return {"body":res}
    else :
        return dataForm("authfail", id["ID"])
        #print("finish")