import requests
import json

slack_webhook_url = ""

def sendSlackWebhook(strText) :
  headers = {
    "Content-tuype" : "application/json"
  }
  data = {
    "text" : strText 
  }

  res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

  if res.status_code == 200 :
    return "OK"
  else :
    return "Error"

print(sendSlackWebhook("안녕하세요. 파이썬에서 보내는 메시지 입니다."))