#pip install pytesseract

from PIL import Image
import pytesseract

##사용 가능한 언어 확인
languages = pytesseract.get_languages(config='')
print(languages)
###

image_path = r'/Users/jyoung/study/40py/22.이미지에서 글자 추출/한글이미지.png'

text = pytesseract.image_to_string(Image.open(image_path), lang="kor+eng")

print(text)

##추출한 텍스트 저장
with open(r'/Users/jyoung/study/40py/22.이미지에서 글자 추출/한글변환.txt','w', encoding='utf8') as f :
  f.write(text)