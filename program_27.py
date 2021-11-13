# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 26, 2021

import matplotlib.pyplot as plt
import pandas as pd

userBorough = input("Enter borough name: ")
userOutputName = input("Enter output name: ")

covidCasesCSV = pd.read_csv("covidCases.csv")

print("Min", covidCasesCSV[userBorough].min())
print("Max", covidCasesCSV[userBorough].max())
print("Mean", covidCasesCSV[userBorough].mean())
print("Median", covidCasesCSV[userBorough].median())
print("Standard Deviation", covidCasesCSV[userBorough].std())

covidCasesCSV['Fraction'] = covidCasesCSV[userBorough]/covidCasesCSV['Case Count']
covidCasesCSV.plot(x = "Date of Interest", y = "Fraction")

fig = plt.gcf()
fig.savefig(userOutputName)