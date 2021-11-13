# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 16, 2021

import turtle

userInputSteps = int(input("Enter number of stamps the turtle will print: "))

wn = turtle.Screen()

turtleSteps = 10
redColor = 186
greenColor = 164
blueColor = 145

myTurtle = turtle.Turtle()
turtle.colormode(255)
myTurtle.shape("circle")
myTurtle.penup()
myTurtle.color(redColor, greenColor, blueColor)

for i in range(userInputSteps):
    myTurtle.pendown()
    myTurtle.stamp()
    myTurtle.penup()

    turtleSteps += 2
    
    if (redColor + 3 <= 255) and (greenColor + 3 <= 255) and (blueColor + 3 <= 255):
        redColor += 3
        greenColor += 3
        blueColor += 3

    myTurtle.color(redColor, greenColor, blueColor)
    myTurtle.forward(turtleSteps)
    myTurtle.right(24)

wn.exitonclick()
