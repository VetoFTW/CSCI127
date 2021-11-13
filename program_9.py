# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 4, 2021

userPhrase = input("Please Enter College: ")
alteredString = ""

for i in userPhrase.split(" "):
    alteredString += i.upper()[0]

print("Reversed phrase:", userPhrase[::-1])
print("Last letter of reversed words:", alteredString[::-1])
