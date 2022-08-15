#pip install qrcode

import qrcode
import os

pwd = os.getcwd()
with open(pwd+'/4qrURL.txt', 'rt', encoding = 'UTF-8') as f :
  read_lines = f.readlines()

  for line in read_lines :
    line = line.strip()
   #print(line)

    qr_data = line
    qr_img = qrcode.make(qr_data)

    save_path = pwd + '/result/4_' + qr_data + '.png'
    qr_img.save(save_path)
    #print(save_path)