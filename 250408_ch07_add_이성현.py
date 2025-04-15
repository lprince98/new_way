############### Chapter 07 ############
########## Additional exam #########
## 1 반복 루프
import random
new_list = []

for i in range(10):
    new_list.append(random.randint(1,101))
print(new_list)

## 2 막대 그래프
list = [26,5,8,13,24,19]
size = len(list)

for i in range(size):
    print(list[i],'*'*list[i])

## 3 색상리스트로 거북이 사각형 그리기
import turtle
import random
t = turtle.Turtle()
t.shape('turtle')

def draw_square(x,y,c):
    c = t.color(c)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()
    
for c in ['yellow','red','purple','blue']:
    x = random.randrange(-200,200)
    y = random.randrange(-200,200)
    draw_square(x,y,c)
turtle.exitonclick()

## 4 별 그리기
import turtle
import random
t = turtle.Turtle()
t.shape('turtle')

s = turtle.Screen()
s.bgcolor('black')

def draw_star(color,length,x,y):
    t.color(color)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.left(144)
    t.end_fill

for color in ['yellow','red','purple','blue','white','gray']*2:
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    length = random.randrange(1,200)
    draw_star(color,length,x,y)
turtle.exitonclick()
