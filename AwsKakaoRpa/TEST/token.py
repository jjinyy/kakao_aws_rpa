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
        "password": "hb1060at^^^"
    })
    response = urllib.request.urlopen(url, data.encode('utf-8'))
    response_body = response.read()
    result = response_body.decode('utf-8')
    return{
            'body':json.dumps(result)['result']
        }
#     access_token = response_body.decode('utf-8')
#     access_token_robot = json.loads(access_token)['result']
    
#     test = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#             {
#                 "simpleText": {
#                     "text": "hi"
#         }
#       }
#     ]
#   }
# }

#     return json.dumps(test)
    
    
    
    
    
    
    #url_robot = "https://154.10.6.152/odata/Robots"
    #url_robot = "https://154.10.6.152/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
    #data_robot = urllib.parse.urlencode({
    #    "startInfo":
    #        {
    #            "ReleaseKey": "b9debd88-73b8-47bd-8e73-e85314e3ad62",
    #            "Strategy": "Specific",
    #            "RobotIds": [8]
    #        }
    #}).encode('utf-8')
    #url_robot.add_header("X-UIPATH-OrganizationUnitId" : "1")
    #url_robot.add_header("Authorization":"Bearer " + format(access_token_robot))
    #request_robot = urllib.request.Request(url_robot, headers = {"X-UIPATH-OrganizationUnitId":"1", "Authorization":"Bearer " + format(access_token_robot)})
    #request_robot = urllib.request.Request(url_robot, data_robot)
    #response_robot = urllib.request.urlopen(request_robot)
    #response_body_robot = response_robot.read()
    #result = response_body_robot.decode('utf-8')
    #return{
    #        'body':json.dumps(result)
    #    }