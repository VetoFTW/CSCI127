# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 26, 2021

import matplotlib.pyplot as plt
import numpy as np

sizeOfCanvas = int(input("Enter the size: "))
outputFileName = input("Enter output file: ")

canvas = np.ones((sizeOfCanvas, sizeOfCanvas, 3))

canvas[1::2, :] = [240 / 256, 230 / 256, 0.5490196347236633]
canvas[:, 1::2] = [0.729411780834198, 143 / 256, 143 / 256]

plt.imsave(outputFileName,canvas)

