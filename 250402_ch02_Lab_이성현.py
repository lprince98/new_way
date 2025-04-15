####### Chapter 02
# Lab exam

radius = 10

print('반지름이',radius,'인 원의 넓이:',radius**2*3.14)

###########

radius = int(input('원의 반지름을 입력하시오:'))
color = input('원의 색깔을 입력하시오:')
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color(color)
t.begin_fill()
t.circle(radius)
t.end_fill()

########### 천둥번개
time = int(input('측정 시간(초) 입력:'))
distance = time * 340
print('자신의 위치에서 번개가 친 장소까지의 거리=',distance,'m')

