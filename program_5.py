# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: August 30, 2021
# This program draws a Rhombus-Flower with the tutle module

import turtle

window = turtle.Screen()
window.bgcolor("khaki")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.fillcolor("green")
myTurtle.pencolor("black")
myTurtle.pensize(3)

angleOne = 45
angleTwo = 135
angleThree = 165

for i in range(6):
    myTurtle.forward(100)
    myTurtle.left(angleOne)
    myTurtle.forward(100)
    myTurtle.left(angleTwo)
    myTurtle.stamp()
    myTurtle.forward(100)
    myTurtle.left(angleOne)
    myTurtle.forward(100)
    myTurtle.right(angleThree)

window.exitonclick()
