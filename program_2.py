# Name: Martin Czarnecki

# Email: martin.czarnecki99@myhunter.cuny.edu

# Date: August 26, 2021

# This program draws a Nonagon for gradescope, and a Hexagon for the lab with the turtle module

# The Hexagon is commented out, for the gradescope grade


import turtle


window = turtle.Screen()

myTurtle = turtle.Turtle()


# For Hexagon

# for i in range(6):

#     myTurtle.forward(150)

#     myTurtle.left(60)


# For Nonagon

for i in range(9):

    myTurtle.forward(75)

    myTurtle.left(40)


window.exitonclick()
