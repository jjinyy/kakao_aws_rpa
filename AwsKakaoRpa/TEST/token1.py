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
    #print(data)
    #print(data.encode('utf-8'))
    response_body = response.read()
    # result = response_body.decode('utf-8')
    # return{
    #         'body':json.dumps(response_body)['result']
    #     }
    access_token = response_body.decode('utf-8')
    access_token_robot = json.loads(access_token)['result']

    return{
            'body':json.dumps(format(access_token_robot))
        }
    
    
    # data_robot = urllib.parse.urlencode({"startInfo":{"ReleaseKey":"b9debd88-73b8-47bd-8e73-e85314e3ad62","Strategy":"Specific","RobotIds":"All"}}).encode('UTF-8')
    # url_robot = urllib.request.Request("https://154.10.6.152/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs")
    # url_robot.add_header("Content-Type","application/json")
    # url_robot.add_header("X-UIPATH-TenantName", "default")
    # url_robot.add_header("X-UIPATH-OrganizationUnitId","1")
    # url_robot.add_header("Authorization","Bearer " + format(access_token_robot))
    
    # result = urllib.request.urlopen(url_robot, data_robot.stringify(data_robot.toJSON())).read().decode('UTF-8')
    # #return{
    # #        'body':json.dumps(result)
    # #    }