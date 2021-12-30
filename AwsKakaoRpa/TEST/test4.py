import json
import base64
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def lambda_handler(event, context):
    headers = {'content-type':'application/json'}
    url = "https://154.10.6.152/api/Account/Authenticate"
    data = {'tenancyName': 'default','usernameOrEmailAddress': 'jjjiny','password': 'hb1060at^^'}
    data = json.dumps(data)
    data_encode = base64.b64encode(bytes(data,'utf-8'))
    request = urllib.request.Request(url, data = data_encode)
    response = urllib.request.urlopen(request)
    #response_body = response.read()
    #print(response_body.decode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)