import json
import base64
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def lambda_handler(event, context):
    post_data  = urllib.parse.urlencode({'tenancyName': 'default','usernameOrEmailAddress': 'jjjiny','password': 'hb1060at^^'}).encode('UTF-8')
    url = urllib.request.Request("https://154.10.6.152/api/Account/Authenticate",post_data)
    url.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64")
    url.add_header("Cookie","webid=x; AGEN=x-tkS8rMRo; SLEVEL=1; TIARA=x-x-5u4SHVdUte-x; webid_sync=x")
    resp= urllib.request.urlopen(url).read().decode('UTF-8')
    #print (resp)
    return{
            'body':json.dumps(resp)
    }