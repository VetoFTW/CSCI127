# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 7, 2021

import matplotlib.pyplot as plt

userInputFile = input("Enter name of the input file: ")
userOutputFile = input("Enter name of the output file: ")

img = plt.imread(userInputFile)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,2] = 0          #Set the blue channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave(userOutputFile, img2)  #Save the image we created to the file: reds.png
