# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 15, 2021

import pandas as pd
import matplotlib.pyplot as plt

userInputFile = input("Enter name of input file:  ")
userOutputFile = input("Enter name of output file:  ")

superBowlFinalsCSV = pd.read_csv(userInputFile)

superBowlFinalsCSV["Date"] = pd.to_datetime(superBowlFinalsCSV["Date"].apply(str))

superBowlFinalsCSV["% Points"] = (superBowlFinalsCSV["Winner Pts"] / (superBowlFinalsCSV["Winner Pts"] + superBowlFinalsCSV["Loser Pts"]) * 100)

superBowlFinalsCSV.plot(x = "Date", y = "% Points", xlabel = "Date")

fig = plt.gcf()
fig.savefig(userOutputFile)