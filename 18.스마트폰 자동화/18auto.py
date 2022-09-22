from ppadb.client import Client
import time

def adb_connect() : 
  client = Client(host='127.0.0.1', port=5037)
  find_devices = client.devices()

  if len(find_devices)==0 :
    print('No devices')
    quit()

  device = find_devices[0]
  print(f'찾은 디바이스: {device}')

  return device, client

device, client = adb_connect()

device.shell('input keyevent 64')
time.sleep(3.0)

#웹 브라우저 열어서 페이지 이동 후 화면 캡처
xyPosition = "10 10"
device.shell(f'input tab {xyPosition}')
time.sleep(2.0)

url = "www.naver.com"
device.shell(f'input text {url}')
time.sleep(2.0)

device.shell(f'input key event 66')
time.sleep(2.0)

result = device.screencap()
with open(r'18.스마트폰 자동화\screen.png','wb') as fp :
  fp.write(result)
