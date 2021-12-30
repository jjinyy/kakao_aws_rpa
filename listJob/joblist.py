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
    
    ###################################################################################
    #작업목록 및 releases key
    res = getToOr(orUrl["Releases"],key,verify=False)
    try :
        joblist = ""
        for i in range(0,100):
            joblist = joblist + res["value"][i]["ProcessKey"] + "\n"
            #print(joblist)
            #print(res["value"][i]["ProcessKey"] + " / " + res["value"][i]["Key"])
    except Exception:
        print(joblist)
        return dataForm("listJob", joblist)
