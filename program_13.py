# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 7, 2021

userInput = input("Enter a list of books and their authors: ")
alteredList = []
errorLog = []

for book in userInput.split(";"):
    alteredList.append(book.split(" "))
    
for i in range(len(alteredList)):
    try:
        alteredList[i].remove("")
    except ValueError as error:
        errorLog.append(error)

for book in alteredList:
    print("{} by {}.{}.".format(book[0], book[2][0], book[3][0]))
