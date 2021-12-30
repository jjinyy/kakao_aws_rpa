import json
import base64
import requests
import urllib.request
import urllib3
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# urllib3.disable_warnings()
  
#Main     
def lambda_handler(event, context): 
    url = "http://192.168.245.50/php/rpa_reserve.php"
    payload = 'FACTORY=PAPER&PROGRAM_ID=RPA001'
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data = payload)
    print(response.text)