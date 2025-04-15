############## Chapter 04 ###########
# Lab 소금물의 농도는?

print('소금물의 농도를 구하는 프로그램입니다.')
salt_gram = int(input('소금의 양은 몇 g입니까?'))
water_gram = int(input('물의 양은 몇 g입니까?'))
per = (salt_gram/water_gram)*100
print('소금물의 농도:%d'% per,'%')

# 간단한 챗봇(CharBot) 프로그램
name = input('''안녕하세요
이름이 뭐예요?''')
len_name = len(name)
print('만나서 반갑습니다.',name,'님\n',name,'님,이름의 길이는 다음과 같군요:',len_name)
age = int(input('나이가 어떻게 돼요?'))
print('내년에는',age+1,'세가 되시는군요')

# 거북이와 인사해봐요
import turtle
t = turtle.Turtle()
t.shape('turtle')
def name_write():
    t.write("안녕하세요?"+name+"씨, 터틀 인사드립니다.")
name = turtle.textinput('Python',"이름을 입력하시오")
name_write()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
name_write()

# 암호 프로그램 만들기
secret = '도서관에서 보자'
print(secret[-1:-9:-1])

# 2050년도에 나는 몇 살?
import time
now = time.time()
thisYear = int(1970+now//(365*24*3600))
print('올해는 '+str(thisYear)+'년입니다.')
age = int(input('당신의 나이를 입력하세요:'))
print('2050년에는 '+str(2050-thisYear+age)+'살이군요')


