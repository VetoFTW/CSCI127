# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 26, 2021

import matplotlib.pyplot as plt
import numpy as np

canvas = np.zeros((30,30,3))

canvas[:, range(6)] = (1, 0, 1)          # Draws left vertical line
canvas[range(6), :] = (1, 0, 1)          # Draws top horizontal line
canvas[range(20), 25:31] = (1, 0, 1)     # Draws right vertical line
canvas[15:21, :] = (1, 0, 1)             # Draws bottom horizontal line

plt.imsave("logo1.png", canvas)