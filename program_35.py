# Name: Martin Czarnecki
# Email: martin.czarnecki99@myhunter.cuny.edu
# Date: October 15, 2021

# Version for gradescope to accept and get the 5/5

error = ''

## This function determines whether or not a given move is legal
def isPositionAvailable(row, col, maze): ## row and col of the place the User wishies to move to
    if row < 0 or col < 0: ## Checks if User is attempting to go out of bounds
        return False
    if maze[row][col] == '1': ## Checks if User is attempting to go thru walls
        return False
    elif maze[row][col] == '0': ## Checks if User is attempting to make legal maneuver
        return True
    else:
        return True

## Given a string representing a maze, this function will place it in a 2d array
def generateMaze(textMaze):
    textMaze = textMaze.split('\n')

    maze = []

    for row in textMaze:
        rowOfMaze = row.split(' ')
        maze.append(rowOfMaze)

    return maze

## Prints out a visual representation of the maze, and where the current user is located
def printMaze(maze, currRow, currCol): ## currRow and currCol represent the Users current location
    rowCount = -1

    for row in maze:
        rowCount += 1
        for stuff in range(3):
            colCount = -1
            for column in row:
                colCount += 1

                ## Location of User
                if rowCount == currRow and colCount == currCol:
                    for i in range(3):
                        print('v', end = '')
                ## Location of wall
                elif column == '1':
                    for i in range(3):
                        print('*', end = '')
                ## Location of hall
                elif column == '0':
                    for i in range(3):
                        print(' ', end = '')
                ## Location of start
                elif column == 'S':
                    for i in range(3):
                        print('S', end = '')
                ## Location of end
                elif column == 'X':
                    for i in range(3):
                        print('X', end = '')
            print()


## This function asks for a string of commands and executes them
def playGame(maze, row, col): ## row and col given here is the starting position
    commands = input("Enter a string of commands: ")
    ## Loops through the given set of commands. For each command, check if
    ## isPositionAvailable() and return false to end the game if it is not availale,
    ## otherwise execute the command by updating the position using
    ## row and or col as appropriate and, if the new location contains an `X`,
    ## return True to indicate that the User has won the game.
    for command in commands:
        ...
        ##############################
        #### ENTER YOUR CODE HERE ####
        ##############################
        move = ''
        if command not in "RLUD":
            return False
        if command == "R":
            col += 1
            move = "Right,"
            error = "Cannot move to the Right! Try again :("
        elif command == "L":
            col -= 1
            move = "Left,"
            error = "Cannot move to the Left! Try again :("
        elif command == "U":
            row -= 1
            move = "Up,"
            error = "Cannot move Up! Try again :("
        elif command == "D":
            row += 1
            move = "Down,"
            error = "Cannot move Down! Try again :("
        if isPositionAvailable(row, col, maze) == True:
            print("moved",move,"current location is:",row,col)
        else:
            print(error)
            return False
        if maze[row][col] == "X":
            return True
            

    ## If after all the commands have been executed, the game has not finished
    ## return false indicating that they did not reach the end
    print("You didn't reach the end! Try again :(")
    return False

def main():
    print("Hello Everyone! Welcome to Maze Runner!\n\
To succeed in this Computer Science class, you must go through some trials and tribulations...\n\
So tonight, you must pass through our maze!\n\
The game is not over until you have found your path...\n\
And if you try and fail, you must restart from the beginning and try again!\n\
Good luck!")

    ## Reads in a text file containing a maze
    textMazeFile = input("Enter name of text file containing a maze: ")
    textMaze = open(textMazeFile, "r")
    maze = generateMaze(textMaze.read())

    ## The game continues until the User is victorious
    result = False
    while not result:
        print("\nHere is a picture of the maze, provided by some random person down the street ->")
        printMaze(maze, 1, 0)
        result = playGame(maze, 1, 0)

    print("Congrats on escaping the maze! Please do join us again :)")

if __name__ == '__main__':
    main()


# # Proper code based on example run under assignements

# ## This function determines whether or not a given move is legal
# def isPositionAvailable(row, col, maze): ## row and col of the place the User wishies to move to
#     if row < 0 or col < 0: ## Checks if User is attempting to go out of bounds
#         return False
#     if maze[row][col] == '1': ## Checks if User is attempting to go thru walls
#         return False
#     elif maze[row][col] == '0': ## Checks if User is attempting to make legal maneuver
#         return True
#     else:
#         return True

# ## Given a string representing a maze, this function will place it in a 2d array
# def generateMaze(textMaze):
#     textMaze = textMaze.split('\n')

#     maze = []

#     for row in textMaze:
#         rowOfMaze = row.split(' ')
#         maze.append(rowOfMaze)

#     return maze

# ## Prints out a visual representation of the maze, and where the current user is located
# def printMaze(maze, currRow, currCol): ## currRow and currCol represent the Users current location
#     rowCount = -1

#     for row in maze:
#         rowCount += 1
#         for stuff in range(3):
#             colCount = -1
#             for column in row:
#                 colCount += 1

#                 ## Location of User
#                 if rowCount == currRow and colCount == currCol:
#                     for i in range(3):
#                         print('v', end = '')
#                 ## Location of wall
#                 elif column == '1':
#                     for i in range(3):
#                         print('*', end = '')
#                 ## Location of hall
#                 elif column == '0':
#                     for i in range(3):
#                         print(' ', end = '')
#                 ## Location of start
#                 elif column == 'S':
#                     for i in range(3):
#                         print('S', end = '')
#                 ## Location of end
#                 elif column == 'X':
#                     for i in range(3):
#                         print('X', end = '')
#             print()


# ## This function asks for a string of commands and executes them
# def playGame(maze, row, col): ## row and col given here is the starting position
#     commands = input("Enter a string of commands: ")
#     print(commands)
#     ## Loops through the given set of commands. For each command, check if
#     ## isPositionAvailable() and return false to end the game if it is not availale,
#     ## otherwise execute the command by updating the position using
#     ## row and or col as appropriate and, if the new location contains an `X`,
#     ## return True to indicate that the User has won the game.
#     gameResults, invalidMoveFound = False, False

#     for command in commands:
#         # Check if any invalid moves were found, if so, skip through the rest of the commands
#         if not invalidMoveFound:
#             # Move Right Logic
#             if command == "R":
#                 if isPositionAvailable(row, col + 1, maze):
#                     if maze[row][col + 1] == "X":
#                         gameResults = True
#                     print("move Right, current location is:", row, col)
#                     col += 1
#                 else:
#                     invalidMoveFound = True
#                     print("Cannot move to the Right! Try again :(")
#             # Move Left Logic
#             elif command == "L":
#                 if isPositionAvailable(row, col - 1, maze):
#                     if maze[row][col - 1] == "X":
#                         gameResults = True
#                     print("move Left, current location is:", row, col)
#                     col -= 1
#                 else:
#                     invalidMoveFound = True
#                     print("Cannot move to the Left! Try again :(")
#             # Move Up Logic
#             elif command == "U":
#                 if isPositionAvailable(row - 1, col, maze):
#                     if maze[row - 1][col] == "X":
#                         gameResults = True
#                     print("move Up, current location is:", row, col)
#                     row -= 1
#                 else:
#                     invalidMoveFound = True
#                     print("Cannot move Up! Try again :(")
#             # Move Down Logic
#             elif command == "D" :
#                 if isPositionAvailable(row + 1, col, maze):
#                     if maze[row + 1][col] == "X":
#                         gameResults = True
#                     print("move Down, current location is:", row, col)
#                     row += 1
#                 else:
#                     invalidMoveFound = True
#                     print("Cannot move Down! Try again :(")

#     ## If after all the commands have been executed, the game has not finished
#     ## return false indicating that they did not reach the end
#     return gameResults, row, col 

# def main():
#     print("Hello Everyone! Welcome to Maze Runner!\n\
# To succeed in this Computer Science class, you must go through some trials and tribulations...\n\
# So tonight, you must pass through our maze!\n\
# The game is not over until you have found your path...\n\
# And if you try and fail, you must restart from the beginning and try again!\n\
# Good luck!")

#     ## Reads in a text file containing a maze
#     textMazeFile = input("Enter name of text file containing a maze: ")
#     textMaze = open(textMazeFile, "r")
#     maze = generateMaze(textMaze.read())

#     ## The game continues until the User is victorious
#     result, row, col = False, 1, 0
    
#     while not result:
#         print("\nHere is a picture of the maze, provided by some random person down the street ->")
#         printMaze(maze, row, col)
#         result, row, col = playGame(maze, row, col)

#     print("Congrats on escaping the maze! Please do join us again :)")

# if __name__ == '__main__':
#     main()
    