#pip install opencv-python

import numpy as np
import cv2
import os,glob

##현재 폴더에 위치한 이미지명 전체 가져오기
path = os.path.dirname(os.path.realpath(__file__))
#os.getcwd()하면 상위 디렉토리를 가져옴 -> 현재 파일의 디렉토리를 가져오도록 변경

pic_list = glob.glob(path+'/*.jpg')  ## 폴더 안에 있는 모든 파일 출력
#glob을 쓰면 파일의 전체경로와 확장자를 지정해서 가져올 수 있음
#print([file for file in file_list if file.endswith('.jpg')])  ## 특정 패턴의 파일만 출력


##openCV
ff = np.fromfile(pic_list[0], np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img  = cv2.resize(img, dsize = (0,0), fx = 1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)


def onChange(pos) :
  pass

#cartoon_img = cv2.stylization(img, sigma_s = 100, sigma_r = 0.1)
cv2.namedWindow("Trackbar Windows")
cv2.createTrackbar("sigma_s","Trackbar Windows",0,200, onChange)
cv2.createTrackbar("sigma_r","Trackbar Windows",0,100, onChange)
cv2.setTrackbarPos("sigma_s","Trackbar Windows",100)
cv2.setTrackbarPos("sigma_r","Trackbar Windows",10)

while True : 
  if cv2.waitKey(100) ==ord('q') :
    break
  
  sigma_s_value = cv2.getTrackbarPos("sigma_s","Trackbar Windows")
  sigma_r_value = cv2.getTrackbarPos("sigma_r","Trackbar Windows") / 100.0

  print("sigma_s_value:", sigma_s_value)
  print("sigma_r_value:", sigma_r_value)

  cartoon_img = cv2.stylization(img, sigma_s = sigma_s_value, sigma_r = sigma_r_value)
  
  cv2.imshow('Trackbar Windows', cartoon_img)

cv2.destroyAllWindows()


#segmentation fault 

