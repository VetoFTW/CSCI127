# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 4, 2021

import turtle

window = turtle.Screen()

userString = "#" + input("Please Enter 6-Digit Hexadecimal: ")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color(userString)

for i in range(4):
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.stamp()
