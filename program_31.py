# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 9, 2021

import pandas as pd
import matplotlib.pyplot as plt

userInputFileName = input("Enter name of input file: ")
userOutputFileName = input("Enter name of output file: ")

homelessShelterCSV = pd.read_csv(userInputFileName)
homelessShelterCSV["Fraction Single Adults"] = homelessShelterCSV["Total Single Adults in Shelter"] / homelessShelterCSV["Total Individuals in Shelter"]
homelessShelterCSV.plot(x = "Date of Census", y = "Fraction Single Adults")

fig = plt.gcf()
fig.savefig(userOutputFileName)