#!/usr/bin/env python
# coding: utf-8

# In[108]:

#pip install selenium
#pip install webdriver-manager

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[109]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 구글 '검색'창의 (selector 추출) 안에 텍스트 입력하여 검색
elem = driver.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[110]:


#페이지 넘겨가며 검색
import time
elem = driver.find_element(By.TAG_NAME, "body")
for i in range(30) : #페이지 다운키를 횟수만큼 반복하여 클릭
  elem.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.1)

try : # '결과 더보기' 버튼이 있으면 눌린 후 페이지 다운 반복
  driver.find_element(By.CSS_SELECTOR, "#islmp > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input").click()
  for i in range(3) : 
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
except :
  pass


# In[115]:


links = []
images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")

#각 이미지 selector를 복사하면 다음과 같음
#islrg > div.islrc > div:nth-child(456) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
#islrg > div.islrc > div:nth-child(458) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# 러개를 한번에 수집하기 위해 (div:nth-child(458)) -> div로 변경

for image in images :
  if image.get_attribute('src') is not None :
    links.append(image.get_attribute('src'))

print('찾은 이미지 개수: ', len(links))


# In[118]:


import urllib.request

links = links[:3]
for k,i in enumerate(links) :
  url = i
  urllib.request.urlretrieve(url, "/Users/jyoung/study/40py/19.구글이미지 크롤링/"+str(k)+".jpg")
  #절대경로로 작성

print("다운로드 완료하였습니다.")


# .ipynb -> .py 로 변환
# 
# pip install nbconvert
# $ jupyter nbconvert --to script 파일명.ipynb
