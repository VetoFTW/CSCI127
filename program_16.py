# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: September 7, 2021

# 1 parsec = 3.26156 light-years. 

print("Please enter the conversion you want to do: \n'a' for Light-Year to Parsec conversion\n'b' for Parsec to Light-Year conversion")

userSelection = input("Your selection: ")

if userSelection == "a":
    userInput = int(input("Please enter a number of Light-Years: "))
    print(userInput, "Light-Years is equal to", userInput / 3.26156)
else:
    userInput = int(input("Please Enter a number of Parsecs: "))
    print(userInput, "Parsecs is equal to", userInput * 3.26156)

    
