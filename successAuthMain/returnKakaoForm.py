import json
import base64
import requests
import urllib.request
import urllib3
import ssl
#from . import test1
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()

#카카오톡 리턴메세지
def dataForm(form,data):
    if form == "auth":
        return {"version": "2.0","template": {"outputs": [{"basicCard": {"title": "권한확인완료!","description": "사용자 " + data + "님의 권한이 확인되었습니다!\n실행 가능한 작업으로 이동해볼까요?","buttons": [{"action": "message","label": "작업으로 이동","messageText": "작업으로 이동"}]}}]}}
    if form == "authfail":
        return {"version": "2.0","template":{"outputs":[{"simpleText": {"text": "권한이 확인되지 않습니다.\n정보가 정확한지 다시 확인해주세요. "}}]}}
    if form == "startJobMsg":
        return {"version": "2.0","template":{"outputs":[{"simpleText": {"text": data + " 작업이 실행되었습니다."}}]}}
    if form == "monitoring":
        return {"version": "2.0","template": {"outputs": [{"basicCard": {"title": "모니터링","description": "원하시는 작업을 선택해주세요.","buttons": [{"action": "message","label": "작업상태","messageText": "작업상태"},{"action":  "webLink","label": "오케스트레이터","webLinkUrl": "https://154.10.6.152"}]}}]}}
    if form == "listJob":
        return {"version": "2.0","template":{"outputs":[{"simpleText": {"text": data}}]}}
    if form == "bottonListMsg":
        return {"version": "2.0","template": {"outputs": [{"basicCard": {"title": "작업 목록","description": "원하시는 작업을 선택해주세요.","buttons": [{"action": "message","label": "작업실행","messageText": "작업리스트"},{"action":  "webLink","label": "작업생성","webLinkUrl": "https://echo.hansol.com/"},{"action": "message","label": "모니터링","messageText": "모니터링"}]}}]}}