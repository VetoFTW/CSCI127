# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: August 30, 2021
# This program draws a Pinwheel with the tutle module

import turtle

window = turtle.Screen()
myTurtle = turtle.Turtle()

myTurtle.shape("arrow")
myTurtle.color("purple")
myTurtle.pensize(3)

myTurtle.forward(30)

for i in range(3):
    for i in range(3):
        myTurtle.forward(50)
        myTurtle.right(120)

    myTurtle.backward(30)
    myTurtle.right(90)
    myTurtle.forward(30)

for i in range(3):
    myTurtle.forward(50)
    myTurtle.right(120)

myTurtle.backward(30)

window.exitonclick()