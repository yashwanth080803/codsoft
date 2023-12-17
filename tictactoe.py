import os
print("WELCOME TO TIC-TAC-TOE")

def printBoard(gameValues):

    print(f" {gameValues[0]} | {gameValues[1]} | {gameValues[2]} ")
    print(f"---|---|---")
    print(f" {gameValues[3]} | {gameValues[4]} | {gameValues[5]} ")
    print(f"---|---|---")
    print(f" {gameValues[6]} | {gameValues[7]} | {gameValues[8]} ")

def checkWin(gameValues):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X'):
            printBoard(gameValues)
            print("X Won the match")
            return 1

        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O'):
            printBoard(gameValues)
            print("O Won the match")
            return 0

        if all(isinstance(item, str) for item in gameValues):
            printBoard(gameValues)
            return -2
    return -1

if __name__ == '__main__':
    print("Welcome to the Game")
    gameValues=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    chance = 1

    while(True):
        try:
            if chance == 1:
                printBoard(gameValues)
                print("\nX's Chance")
                value = int(input("\nPlease enter a value: "))

                if gameValues[value]!= 'O':
                    gameValues[value] = 'X'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for X")
                    continue
                os.system('CLS')

            if chance == 0:
                printBoard(gameValues)
                print("\nZ's Chance")
                value = int(input("\nPlease enter a value: "))

                if gameValues[value]!= 'X':
                    gameValues[value] = 'O'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for O")
                    continue
                os.system('CLS')

        except IndexError:
            os.system('CLS')
            print("\nOops!! Please Enter value from 0 - 8\n")
            continue

        chance = 1 - chance
        cwin = checkWin(gameValues)
        if(cwin == -2):
            print("Game Draw")
            break
        if(cwin != -1):
            print("Match over")
            break