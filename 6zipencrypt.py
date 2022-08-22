import itertools
import zipfile

def unzip(passwd_string, min_len, max_len, zFile) :
    for lan in range(min_len,max_len) :
        #암호 문자열 brute-force로 생성
        to_attempt = itertools.product(passwd_string, repeat = lan)
        for attampt in to_attempt :
            passwd = ''.join(attampt)
            print(passwd)

            try :
                zFile.extractall(pwd = passwd.encode())
                print(f'비밀번호는 {passwd} 입니다.')
                return 1
            except :
                pass


passwd_string = "012345"
#56789abcdefghijklmnopqrstuvwxyz

#대상파일
zFile = zipfile.ZipFile('6zip.zip')
try :
    zFile.extractall(pwd = '123'.encode())
    print(f'비밀번호 해제 성공')
except :
    pass

min_len = 3
max_len=4
unzip_result = unzip(passwd_string, min_len, max_len, zFile)

    
    