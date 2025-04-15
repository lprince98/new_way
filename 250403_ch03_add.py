#1
chicken = int(input('닭의 수:'))
pig = int(input('돼지의 수:'))
cow = int(input('소의 수:'))
num_leg = (chicken * 2) + (pig + cow) * 4
print('전체 다리의 수:',num_leg)

#2
x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2:'))
result = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('두 점 사이의 거리=',result)

#3
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.setheading(45)
t.forward(141.4)
t.right(45)
t.up()
t.goto(0,0)
t.down()
t.forward(100)
t.left(90)
t.forward(100)

#4
import turtle
t = turtle.Turtle()
t.shape('turtle')

x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2:'))
result = str(((x2-x1)**2 + (y2-y1)**2)**0.5)

def name_write():
    t.write("점의 길이="+result)
t.goto(x1,y1)
t.goto(x2,y2)
name_write()

#5
import time
cur_time = time.time()
cur_min = cur_time//3600

cur_min_1 = int((cur_time%3600)//60)

cur_hour = int(cur_min%24)
print('현재 시간(영국 그리니치 시각):',cur_hour,'시',cur_min_1,'분')