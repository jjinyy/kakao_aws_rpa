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
    return dataForm("screenshot", None)