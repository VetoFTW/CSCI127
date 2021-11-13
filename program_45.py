# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: November 1, 2021

import pandas
import folium

userInputFileName = input("Please enter the name of the input file: ")
userOutputFileName = input("Please enter the name of the output file: ")
userDesiredBorough = input("Please enter the name of the borough: ")

# userInputFileName = "NYC_Wi-Fi_Hotspot_Locations.csv"
# userOutputFileName = "manhattan.html"
# userDesiredBorough = "Brooklyn"

wifiCSV = pandas.read_csv(userInputFileName)

myMap = folium.Map(location=[40.768731, -73.964915], tiles="Stamen Watercolor")

for index, row in wifiCSV.iterrows():
    if row["City"] == userDesiredBorough:
        folium.Marker(location=[row["Latitude"], row["Longitude"]], popup=row["Location"]).add_to(myMap)

myMap.save(outfile=userOutputFileName)

