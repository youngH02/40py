#pip install opencv-python
#https://pixabay.com/ko/

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

#openCV에서 한글경로를 읽지 못해 np로 파일을 가져옴
ff = np.fromfile(r'/Users/jyoung/study/40py/23.사진에서 얼굴모자이크(OpenCV)/사람들.jpg', np.uint8) 
#np의 이미지를 openCV로 불러옴
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
#이미지 크기조절
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

#회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#얼굴을 찾아 파란색 네모 표시
#여러개의 얼굴을 찾음 scalefactor는 감도, minNeighbor은 최소 이격 거리
faces = face_cascade.detectMultiScale(gray, 1.2,5 )
for (x,y,w,h) in faces :
  cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)

  roi_gray = gray[y:y+h, x:x+w]
  roi_color = img[y:y+h, x:x+h]
  
  #눈을 찾아 녹색 네모 표시
  eyes = eye_casecade.detectMultiScale(roi_gray)
  for (ex,ey,ew,eh) in eyes : 
    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()