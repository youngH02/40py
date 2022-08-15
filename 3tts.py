# pip install gtts #문자를 음성으로 변호나해주는 라이브러리
# pip install playsound #mp3파일을 파이썬에서 재생

from gtts import gTTS
from playsound import playsound
import os

pwd = os.getcwd()

with open(pwd+'/3ttsinput.txt','rt',encoding='UTF-8') as f:
  read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
save_path = pwd + '/result/3_hi' + '.mp3'
tts.save(save_path)
print(save_path)
playsound('/Users/jyoung/study/40py/result/3_hi.mp3')

#경로를 .py파일의 실행결로로 이동, 현재 경로로 이동
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())
# tts.save("hi.mp3")
# playsound("hi.mp3")
