########### Chapter 06 ###########
####### Lab #######
## 1 코드를 줄여보아요
import turtle
t = turtle.Turtle()
t.shape('turtle')

for i in range(1,7):
    t.circle(100)
    t.left(60)

## 2 도돌이표
print('연주순서:')
print('A', end = " ")
print('B', end = " ")
for i in range(2):
    print('C', end = " ")
    print('D', end = " ")

## 3 n각형 그리기
import turtle
t = turtle.Turtle()
t.shape('turtle')

num_angle = (int(turtle.textinput('python','몇 각형을 원하시나요?')))
angle = 360/num_angle
for i in range(1,num_angle+1):
    t.forward(100)
    t.left(angle)

## 4 랜덤 워크 시뮬레이션
import turtle
t = turtle.Turtle()
t.shape('turtle')

import random    
num_random = random.randint(1,100)
print(num_random)

for i in range(1,num_random):
    rand_angle = random.randint(0,361)
    rand_dist = random.randint(0,100)
    t.forward(rand_dist)
    t.setheading(rand_angle)

## 5 범인 찾기 게임
import random
room_num = random.randint(1,4)
num = int(input('어느 방에 숨었을까요?'))
reward = 0

while room_num != num:
    reward -= 10
    print(reward)
    room_num = random.randint(1,4)
    num = int(input('어느 방에 숨었을까요?'))
reward += 100
print(reward)

## 6 몬드리안 터틀
import turtle, random
t = turtle.Turtle()
t.shape('turtle')

num_trial = random.randint(1,11)
for i in range(num_trial):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(10,300)
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r,g,b)
    t.begin_fill()
    for j in range(2):
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)
    t.end_fill() 

## 7 모든 약수 구하기
num = int(input('자연수 입력:'))
result = 0

for i in range(1,num+1):
    if num%i == 0:
        print(i,end=" ")

## 8 최대공약수 구하기
int_1 = int(input('정수1 입력:'))
int_2 = int(input('정수2 입력:'))
if int_1>int_2:
    int_high = int_1
    int_low = int_2
else:
    int_high = int_2
    int_low = int_1

while int_high%int_low > 0:
    int_high, int_low = int_low, int_high%int_low
if int_low == 1:
    print('두 수는 서로소이다.')
else:
    print('두 수의 최대공약수:', int_low)

## 9 별 그리는 터틀
import turtle
t = turtle.Turtle()
t.shape('turtle')

for i in range(5):
    t.forward(100)
    t.right(144)

## 10 숫자 맞추기 게임
import random
num_random = random.randrange(1,101)
print('1부터 100 사이의 숫자를 맞추시오')
num = int(input('숫자를 입력하시오:'))
n = 1
while num != num_random:
    n += 1
    if num > num_random:
        print('낮음!')
    elif num < num_random:
        print('높음!')
    num = int(input('숫자를 입력하시오:'))
print('축하합니다.시도횟수:', n) 