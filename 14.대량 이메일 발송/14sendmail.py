import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


send_email = '메일주소@gmail.com'
send_pwd = '메일앱비밀번호'

recv_email = '수신 이메일주소'

#smtp_name = 'smtp.naver.com'
smtp_name = 'smtp.gmail.com'
smtp_port = 587


#msg = MIMEText(text) #텍스트 형태로 발송
msg = MIMEMultipart() #메시지를 복합형식으로 선언 - 첨부파일 발송 가능

msg['Subject'] = '메일 제목 : 40py로 발송하는 메일'
msg['From'] = send_email
msg['To'] = recv_email
text = '''메일 내용 입력'''

contentPart = MIMEText(text)
msg.attach(contentPart)

#파일 첨부
etc_file_path = r'14.대량 이메일 발송/이메일첨부.txt'
with open(etc_file_path, 'rb') as f :
  etc_part = MIMEApplication(f.read())
  etc_part.add_header('Content_Disposition','attachment',filename="abc.txt")
  msg.attach(etc_part)

print(msg.as_string())
#메일 발송되는 코드
s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

