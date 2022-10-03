from time import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json

driver = webdriver.Chrome('21.핫딜알리미/chromedriver')

send_message_list = []
slack_webhook_url = ""
URL = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'

def sendSlackWebhook(strText) :
  headers = {
    "Content-tuype" : "application/json"
  }
  data = {
    "text" : strText 
  }

  res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

  if res.status_code == 200 :
    return "OK "+ strText
  else :
    return "Error "+strText

while True :
	try :
		driver.get(url=URL)
		titles = driver.find_elements(By.CSS_SELECTOR,'#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
		urls = driver.find_elements(By.CSS_SELECTOR,'#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')
		message = ""
		
		for i in range(len(titles)) :
			if "갈비탕" in titles[i].text :
				message = titles[i].text+"\n"+ urls[i].get_attribute("href")
				if message not in send_message_list : 
					print(sendSlackWebhook(message))
					send_message_list.append(message)
		time.sleep(60.0 *5)
		
	except KeyboardInterrupt :
		break
        





  
