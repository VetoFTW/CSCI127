# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 27, 2021

import matplotlib.pyplot as plt

userInputImageOne = plt.imread(input("Enter first image file name: "))
userInputImageTwo = plt.imread(input("Enter second image file name: "))
userInputThreshold = float(input("Enter threshold of white pixels: "))

snowCountOfFirstImage = 0
snowCountOfSecondImage = 0

# Count for first Image
for i in range(userInputImageOne.shape[0]):
    for j in range(userInputImageOne.shape[1]):
        if (userInputImageOne[i][j][0] > userInputThreshold) and (userInputImageOne[i][j][1] > userInputThreshold) and (userInputImageOne[i][j][2] > userInputThreshold):
            snowCountOfFirstImage += 1

# Count for second Image
for i in range(userInputImageTwo.shape[0]):
    for j in range(userInputImageTwo.shape[1]):
        if (userInputImageTwo[i][j][0] > userInputThreshold) and (userInputImageTwo[i][j][1] > userInputThreshold) and (userInputImageTwo[i][j][2] > userInputThreshold):
            snowCountOfSecondImage += 1

# Print
print("Snow count of first image:", snowCountOfFirstImage)
print("Snow count of second image:", snowCountOfSecondImage)
print("Difference between first and second image:", abs(snowCountOfFirstImage - snowCountOfSecondImage))

