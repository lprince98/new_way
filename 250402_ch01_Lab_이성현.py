##### Chapter 01
# Lab. print()실습

print('9*8은 72입니다.')

print('너무','반짝'*2,'눈이 부셔','No '*5)
print('너무','깜짝'*2,'놀란 나는','Oh '*5)
print('너무','짜릿'*2,'몸이 떨려','Gee '*5)

# Lab. 원과 다각형 그리기
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.circle(100)

#################

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)

#################

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.width(10)
t.forward(100)
t.left(90)
t.forward(100)

#################

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.forward(100)
t.left(90)
t.forward(100)

#################

import turtle
t = turtle.Turtle()
t.shape('square')
t.forward(100)
t.left(90)
t.forward(100)

#################

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.down()
t.goto(100,0)
t.up()
t.goto(0,200)
t.down()
t.goto(100,200)
