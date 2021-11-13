# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: August 26, 2021
# This program takes an input phrase, reprints
# the phrase in 3 variations, and searches for
# the number of times a character appears

phrase = input(print("Enter a message: "))
letterToSearch = input(print("Enter a letter: "))

print(phrase)
print(phrase.upper())
print(phrase.lower())
print(phrase.count(letterToSearch))



