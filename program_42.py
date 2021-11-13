# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 23, 2021

import folium
map = folium.Map(location=[40.75,-74.125])
folium.Marker(location=[40.7420577, -74.0101494], popup="Little Island").add_to(map)
map.save(outfile="nycMap.html")