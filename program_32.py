# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 9, 2021

import matplotlib.pyplot as plt
import pandas as pd

userInputFileName = input("Enter name of input file: ")
userOutputFileName = input("Enter name of output file: ")

ufoSightingsCSV = pd.read_csv(userInputFileName)

topTenStates = ufoSightingsCSV.groupby("state")["duration (seconds)"].mean().sort_values(ascending=False)[:10]

groupedGraph = topTenStates.plot.bar(xlabel="State", ylabel="Seconds")

fig = plt.gcf()
fig.savefig(userOutputFileName)