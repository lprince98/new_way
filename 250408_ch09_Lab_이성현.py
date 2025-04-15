########### Ch09 ###########
#### Lab exam ####
# 1 가위 바위 보 게임
# import random
# computer = random.choice(['가위','바위','보'])
# player = input('가위, 바위 보 입력:')

# if player == '가위':
#     if player == computer:
#         print('비겼습니다.')
#     elif player != computer:
#         if computer == '보':
#             print('이겼습니다.')
#         elif computer == '바위':
#             print('졌습니다.')
# if player == '바위':
#     if player == computer:
#         print('비겼습니다.')
#     elif player != computer:
#         if computer == '가위':
#             print('이겼습니다.')
#         elif computer == '보':
#             print('졌습니다.')
# if player == '보':
#     if player == computer:
#         print('비겼습니다.')
#     elif player != computer:
#         if computer == '바위':
#             print('이겼습니다.')
#         elif computer == '가위위':
#             print('졌습니다.')

## 2 행성까지의 여행 시간은?
# planet = {'수성':917,'금성':414,'화성':784,'목성':6287,'토성':12774,'천왕성':27504,'해왕성':43474}
# planet_name = input('행성 이름:')
# velocity = float(input('이동 속도(km/k):'))

# if planet_name in planet:
#     time = planet[planet_name]*100000 / velocity
#     print('이동 시간:%d 시간'%time)
#     year = int(time) // (365*24)
#     month = int(time - (year*365*24)) // (30*24)
#     day = int(time - (year*365*24) - (month*30*24)) // 24
#     hour = int(time - (year*365*24) - (month*30*24) - (day*24))
# print('이동시간: 약 %d년 %d월 %d일 %d시간'% (year,month,day,hour))

## 3 파이썬으로 e-mail 보내기
import smtplib
from email.mime.text import MIMEText

my_email = 'lilprince98@gmail.com'
to_email = 'bluesea0228@hanmail.net'
contents = '첫 번째 파이썬으로 메일 보내기'

msg = MIMEText(contents, _charset='euc-kr')
msg['Subject'] = '첫 번째 파이썬으로 메일 보내기'
msg['From'] = my_email
msg['To'] = to_email

google_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
google_server.login('lilprince98','ffbz qghc haml yadx')
google_server.sendmail(my_email,to_email,msg.as_string())
google_server.quit()