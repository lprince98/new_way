######## Chapter 03 ########
# Lab 다항식의 계산

x = -1
y = 3

result = -y**3 + 2*x**2*y
print(result)

#######################
# Lab 화시온도를 섭씨 온도로 변환하기

tem_f = int(input('화씨온도:'))
tem_c = (tem_f-34)*5/9
print(tem_c)

#######################
# Lab 두점 사이의 거리 구하기
x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2:'))
result = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('두 점 사이의 거리=',result)


#######################
# Lab 두점 사이의 거리 확인하기
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.left(45)
t.forward(141.4)
t.right(45)
t.up()
t.goto(0,0)
t.down()
t.forward(100)
t.left(90)
t.forward(100)

######################
# Lab 두 점 사이의 거리 확인하기
import turtle
t = turtle.Turtle()
t.shape('turtle')
angle = int(input('머리 방향:'))
t.setheading(angle)

######################
# Lab 그리니치 표준시 - 세계시간의 기준점
import time
cur_time = time.time()
cur_min = cur_time//3600

cur_min_kor = (cur_time%3600)/60

cur_hour = cur_min%24
cur_hour_kor = cur_hour + 9
print('현재 한국 시간:',cur_hour_kor,'시',cur_min_kor,'분')


######################
# Lab 계산대 프로그램
mon = int(input('투입한 돈:'))
price = int(input('물건가격:'))
change = mon-price
cha_500 = change // 500
cha_100 = (change-(cha_500*500))//100
print('거스름돈:',change)
print('500원 동전의 개수:',cha_500)
print('100원 동전의 개수:',cha_100)
