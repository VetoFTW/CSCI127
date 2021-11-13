# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 20, 2021

import random

isGameRunning = True
winner = ""

while isGameRunning:

    userMove = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: "))

    if userMove < 1:
        isGameRunning = False

    programMove = random.randint(1,3)
    print("computerMove:", programMove)

    if userMove > 3:
        winner = "invalid"

    elif userMove - programMove == 0:   winner = "draw"

    elif userMove == 1:
        if programMove == 3:    winner = "human"
        else:   winner = "computer"
   
    elif userMove == 2:
        if programMove == 1:    winner = "human"
        else:   winner = "computer" 

    elif userMove == 3:
        if programMove == 2:    winner = "human"
        else:   winner = "computer"

    print("round finished and winner is:", winner)
