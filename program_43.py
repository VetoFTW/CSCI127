# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: November 1, 2021

from os import name
from matplotlib.pyplot import title
import pandas as pd
import folium

userInputFileName = input("Enter CSV file name: ")
userOuputFileName = input("Enter output file: ")

# userInputFileName = "attractions.csv"
# userOuputFileName = "thMap.html"

attractionsCSV = pd.read_csv(userInputFileName)

map = folium.Map(location=[40.768731, -73.964915], tiles="Cartodb Positron")

for index, row in attractionsCSV.iterrows():
    folium.Marker(location=[row["LONGITUDE"], row["LATITUDE"]], popup=row["NAME"]).add_to(map)
    
map.save(outfile=userOuputFileName)