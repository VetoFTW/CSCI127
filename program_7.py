# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: August 26, 2021
# This program shifts all letters in a phrase +5 in ascii table

phrase = input(print("Enter a message: "))

for char in phrase:
    print(char, "shifted by 5 characters is:", chr(ord(char) + 5) )