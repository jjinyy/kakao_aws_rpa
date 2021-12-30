import json
import base64
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def lambda_handler(event, context):
    post_data  = urllib.parse.urlencode({'tenancyName': 'default','usernameOrEmailAddress': 'jjjiny','password': 'hb1060at^^'}).encode('UTF-8')
    url = urllib.request.Request("https://154.10.6.152/api/Account/Authenticate", post_data)
    url.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64")
    url.add_header("Cookie","webid=x; AGEN=x-tkS8rMRo; SLEVEL=1; TIARA=x-x-5u4SHVdUte-x; webid_sync=x")
    resp= urllib.request.urlopen(url).read().decode('UTF-8')
    access_token_robot = json.loads(resp)['result']
    
    return{
            'body':json.dumps(access_token_robot)
    }

    # data_robot = urllib.parse.urlencode({"startInfo":{"ReleaseKey": "b9debd88-73b8-47bd-8e73-e85314e3ad62","Strategy": "Specific","RobotIds": "All"}}).encode('UTF-8')
    # url_robot = urllib.request.Request("https://154.10.6.152/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs")
    # url_robot.add_header("Content-Type","application/json")
    # url_robot.add_header("X-UIPATH-TenantName", "default")
    # url_robot.add_header("X-UIPATH-OrganizationUnitId","1")
    # url_robot.add_header("Authorization","Bearer " + format(access_token_robot))
    
    # result = urllib.request.urlopen(url_robot, data_robot).read().decode('UTF-8')
    
    # return{
    #         'body':json.dumps(result)
    # }