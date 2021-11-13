# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 9, 2021

import pandas as pd

userInputNameFile = input("Enter file name: ")

ramenCSV = pd.read_csv(userInputNameFile)
ramenCSV["Stars"] = pd.to_numeric(ramenCSV["Stars"], downcast="float")

#  The Average Stars Per Style
print("The average stars per serving style:")
print(ramenCSV.groupby("Style")["Stars"].mean())

# The Least Rated Ramon Spot In Singapore
singaporeRomanLowestReviews = ramenCSV.groupby("Country").get_group("Singapore").groupby("Brand")["Stars"].min()
singaporeBrandLowestReview = singaporeRomanLowestReviews.idxmin(axis=0)

print(singaporeBrandLowestReview, "has the lowest rating in Singapore with", singaporeRomanLowestReviews[singaporeBrandLowestReview], "stars.")

