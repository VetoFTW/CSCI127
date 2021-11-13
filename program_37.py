# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 9, 2021

from os import sep
import pandas as pd

userInputName = input("Enter file name: ")
vgSalesCSV = pd.read_csv(userInputName)

print("There are", vgSalesCSV.count().get("Rank"), "total games")
print("The number of game in each genre are", vgSalesCSV.groupby("Genre")["Name"].count().sort_values(ascending=False), sep="\n")
print("The top 3 game publishers are", vgSalesCSV.groupby("Publisher")["Name"].count().sort_values(ascending=False)[:3], sep="\n")
