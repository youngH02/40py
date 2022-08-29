#pip install googletrans==4.0.0-rc1

import googletrans
from os import linesep
langs = googletrans.LANGUAGES
print(langs)

translator = googletrans.Translator()

# str1 = '행복하세요'
# result1 = translator.translate(str1, dest='en', src='auto')
# print(f'{str1} => {result1.text}')

# str2 = 'haappy'
# result2 = translator.translate(str2, dest='ko', src='auto')
# print(f'{str2} => {result2.text}')

read_file = '9eng.txt'
write_file = '9trans.txt'
with open(read_file, 'r') as f:
  readLines = f.readlines()

for lines in readLines :
  result = translator.translate(lines, dest='ko')
  print(result)
  with open(write_file, 'a', encoding='UTF-8') as f :
    f.write(result.text+'\n')