# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: November 1, 2021

import numpy as np
import matplotlib.pyplot as plt

print("------------------------------------------", "Welcome to the Color Maker!", "------------------------------------------", sep="\n")
print("Please enter for each rbg color the value in which to increase/decrease them.", "If all 3 values given are 0, the program will end and save the resulting image.", sep="\n")

outputFile = input("Enter outfile name: ")

myCanvas = np.zeros((10, 10, 3))

myColor = [0, 0, 0]
isRunning = True
while isRunning:
    
    updatedRed = int(input("How much do you want to change the red value by? "))
    updatedGreen = int(input("How much do you want to change the green value by? "))
    updatedBlue = int(input("How much do you want to change the blue value by? "))

    if updatedRed == 0 and updatedGreen == 0 and updatedBlue == 0:
        myCanvas[:, :] = myColor
        plt.imsave(outputFile, myCanvas)
        print("You're done! Congrats on the color, it looks beautiful!")
        isRunning = False

    else:
        if myColor[0] + (updatedRed / 255) >= 1: myColor[0] = 1.0
        else: myColor[0] += (updatedRed / 255)

        if myColor[1] + (updatedGreen / 255) >= 1: myColor[1] = 1.0
        else: myColor[1] += (updatedGreen / 255)

        if myColor[2] + (updatedBlue / 255) >= 1: myColor[2] = 1.0
        else: myColor[2] += (updatedBlue / 255)

        print("The current rgb values are:", myColor)
