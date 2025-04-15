##################### Chapter 08 #########
######## additional exam ######
## 1 함수 그래프
import turtle
t = turtle.Turtle()
t.shape('turtle')

t.goto(200,0)
t.up()
t.goto(0,0)
t.down()
t.goto(0,200)
t.goto(0,0)

def func(x):
    result = x**2+1
    return result

for x in range(150):
    result = func(x)*0.01
    t.goto(x, result)
turtle.exitonclick()

## 2 덧셈, 뺄셈, 곱셈, 나눗셈 함수
def add(x,y):
    result = x+y
    return result
def subtraction(x,y):
    result = x-y
    return result
def multiplication(x,y):
    result = x*y
    return result
def division(x,y):
    result = x/y
    return result

x = int(input('x:'))
y = int(input('y:'))
print(x,'+',y,'=',add(x,y))
print(x,'-',y,'=',subtraction(x,y))
print(x,'*',y,'=',multiplication(x,y))
print(x,'/',y,'=',division(x,y))

## 3 소수 검사
def testPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

for j in range(2,101):
    if testPrime(j):
        print(j, end=" ")
