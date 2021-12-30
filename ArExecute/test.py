import requests
from returnKakaoForm import dataForm
# ssl._create_default_https_context = ssl._create_unverified_context
# urllib3.disable_warnings()
  
#Main
def lambda_handler(event, context): 
    url = "http://154.10.8.151:8012/api/rpa_reserve.php"
    factory = event["action"]["params"]["FACTORY"]
    program_id = event["action"]["params"]["PROGRAM_ID"]
    user_id = event["action"]["params"]["USER_ID"]
    
    factory = factory.upper()
    program_id = program_id.upper()
    
    payload = 'FACTORY='+factory+'&PROGRAM_ID='+program_id+'&USER_ID='+user_id
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data = payload)
    #print(response.text)
    
    result = response.text.split("@")
    
    if result[1] == "True":
        data = user_id + "님이 요청하신" + factory + " 공장의 " + program_id + "업무가 예약되었습니다.\n가능한 빠르게 요청해주신 업무가 실행됩니다."
    if result[1] == "False":
        data = result[2]
    
    #print(result[1] + result[2])
    
    #if (response != None):
    return dataForm("arStart",data)
        
    #return(response.text)