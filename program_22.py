# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 26, 2021

import turtle

wn = turtle.Screen()
wn.bgcolor("khaki")
turtle.colormode(255)

myTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.pensize(5)

for i in range(36):
    myTurtle.pencolor(0, i * 7, 0)
    myTurtle.forward(10)
    myTurtle.left(10)
    
    for j in range(4):
        myTurtle.left(90)
        myTurtle.forward(300)
        myTurtle.backward(50)
        
wn.exitonclick()