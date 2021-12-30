import json
import base64
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def lambda_handler(event, context):
    url = "https://154.10.6.152/api/Account/Authenticate"
    request = urllib.request.Request(url)
    data = urllib.parse.urlencode({
        "tenancyName": "default",
        "usernameOrEmailAddress": "jjjiny",
        "password": "hb1060at^^"
    })
    response = urllib.request.urlopen(request, data.encode('utf-8'))
    
    response_body = response.read()
    result = response_body.decode('utf-8')
    
    return{
            'statusCode':200,
            'body':json.dumps(result)
        }
    
    
    #if(rescode==200):
    #    response_body = response.read()
    #    print(response_body.decode('utf-8'))
    #else:
    #    print("Error Code:" + rescode)