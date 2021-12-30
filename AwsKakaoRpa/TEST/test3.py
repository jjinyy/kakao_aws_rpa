import json
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def lambda_handler(event, context):
    url = "https://154.10.6.152/api/Account/Authenticate"
    request = urllib.request.Request(url)
    #request = urllib.request.urlopen(url)
    data = urllib.parse.urlencode({
        "tenancyName": "default",
        "usernameOrEmailAddress": "jjjiny",
        "password": "hb1060at^^"
    })
    response = urllib.request.urlopen(request, data.encode('utf-8'))
    #response = urllib.request.urlopen(request, data = data)
    response_body = response.read()
    #print(response_body)
    print(response_body.decode('utf-8'))
    #rescode = response.getcode()
    #if(rescode==200):
    #    response_body = response.read()
    #    print(response_body.decode('utf-8'))
    #else:
    #    print("Error Code:" + rescode)