########### Chapter 05 #########
########### Lab exam ######
## 1 직각삼각형 판별하기
a = int(input('변a의 길이:'))
b = int(input('변b의 길이:'))
c = int(input('변c의 길이:'))
cal = a**2+b**2
if c < a+b:
    if cal != c**2:
        print('직각삼각형이 아닙니다.')
    else:
        print('직각삼각형입니다.')
else: print('삼각형이 아닙니다.')

## 2 정수의 종류를 판별하는 스마트 터틀
import turtle
t = turtle.Turtle()
t.shape('turtle')

num = int(turtle.textinput('Python','숫자를 입력하시오.'))
if num > 0:
    t.goto(0,0)
    t.goto(100,100)
    name = t.write('입력된 정수는 양의 정수입니다.')
elif num == 0:
    t.goto(0,0)
    t.goto(100,0)
    name = t.write('입력된 정수는 0입니다.')
else:
    t.goto(0,0)
    t.goto(100,-100)
    name = t.write('입력된 정수는 음의 정수입니다.')

## 3 주민등록번호 뒷자리 의미, 이런 뜻?!
import random
ran_num = random.randrange(1,5)
print('주민등록번호의 성별 정보 번호를 생성합니다.')
if ran_num == 1 or ran_num == 3:
    print('생성번호:',ran_num)
    print('남성입니다.')
else:
    print('생성번호:',ran_num)
    print('여성입니다.')
print('프로그램을 종료합니다.')

## 4 동전 던지기 게임
from turtle import *
import random
ran_num = random.randrange(1,3)
screen = Screen()

if ran_num == 1:
    image_front = screen.bgpic("C:/Users/blues/OneDrive/Desktop/front.gif")
    print('앞면',image_front)

else:
    image_back = screen.bgpic("C:/Users/blues/OneDrive/Desktop/back.gif")
    print('뒷면',image_back)

## 5. 찌릿찌릿 전기회로
bat_1 = input('1번 전지가 있습니까? (Y/N)')
bat_2 = input('2번 전지가 있습니까? (Y/N)')

if bat_1 == 'y' and bat_2 == 'y':
    print('직렬연결 : 전구에 불이 켜집니다.')
    print('병렬연결 : 전구에 불이 켜집니다.')
elif bat_1 == 'y' or bat_2 == 'y':
    print('직렬연결 : 전구에 불이 꺼집니다.')
    print('병렬연결 : 전구에 불이 켜집니다.')
else:
    print('직렬연결 : 전구에 불이 꺼집니다.')
    print('병렬연결 : 전구에 불이 꺼집니다.')

## 6. 윤년 판단
year = int(input('연도를 입력하시오:'))
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(str(year)+' 년은 윤년입니다.')
else: print(str(year)+' 년은 윤년이 아닙니다.')

## 7 이차방정식의 판별식
a = int(input('a값 입력:'))
b = int(input('b값 입력:'))
c = int(input('c값 입력:'))
d_cal = b**2-(4*a*c)
if d_cal > 0:
    print('방정식은 서로 다른 두 실근입니다.')
elif d_cal == 0:
    print('방정식은 서로 다른 두 실근(중근)입니다.')
else: print('방정식은 서로 다른 두 허근입니다.')

## 8 사용자가 원하는 도형 그리기
import turtle
t = turtle.Turtle()
t.shape('turtle')

shape = turtle.textinput('python','도형을 입력하시오')
if shape == '직사각형':
    width = int(turtle.textinput('python','가로:'))
    height = int(turtle.textinput('python','세로:'))
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
elif shape == '정삼각형':
    length = int(turtle.textinput('python','한 변의 길이:'))
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
elif shape == '원':
    radius = int(turtle.textinput('python','반지름의 길이:'))
    t.circle(radius)

## 9 두 원의 위치 관계 시뮬레이션
import turtle
t = turtle.Turtle()
t.shape('turtle')

x1 = int(input('큰 원의 중심좌표 x1:'))
y1 = int(input('큰 원의 중심좌표 y1:'))
r1 = int(input('큰 원의 반지름:'))
x2 = int(input('작은 원의 중심좌표 x2:'))
y2 = int(input('작은 원의 중심좌표 y2:'))
r2 = int(input('작은 원의 반지름:'))

t.up()
t.goto(x1,y1-r1)
t.down()
t.circle(r1)
t.up()
t.goto(x2,y2-r2)
t.down()
t.circle(r2)

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

if distance == 0:
    turtle.write("동심원")
elif distance == r1- r2:
    turtle.write('내접')
elif r1-r2 < distance < r1+r2:
    turtle.write('두 점에서 만납니다.')
elif distance > r1+r2:
    turtle.write('만나지 않고 외부에 있습니다.')
elif distance == r1+r2:
    turtle.write('외접')
elif distance < r1-r2:
    turtle.write('만나지 않고 내부에 있습니다.')