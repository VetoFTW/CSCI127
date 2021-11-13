# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 6, 2021

userInput = input("Enter a word: ")
encryptedInput = ""

for char in userInput:
    if ord(char) + 13 > 90:
        encryptedInput += chr(ord(char) + 13 - 26)
    else:
        encryptedInput += chr(ord(char) + 13)

print("Your word in code is", encryptedInput)
