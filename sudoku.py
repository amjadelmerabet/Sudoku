import random


def initialize_table(tab,values):
    for i in range(9):
        for j in range(9):
            tab[i][j] = values[i][j]

def draw_table(tab):
    for i in range(9):
        if i == 3 or i == 6:
            print("+---+---+---+ +---+---+---+ +---+---+---+")
        print("+---+---+---+ +---+---+---+ +---+---+---+")
        for j in range(9):
            if j % 3 == 0 :
                if j != 0:
                    print(end = " ")
                print("|",end = "")

            if tab[i][j] == 0:
                print("   |",end = "")
            elif tab[i][j] == 1:
                print(" 1 |",end = "")
            elif tab[i][j] == 2:
                print(" 2 |",end = "")
            elif tab[i][j] == 3:
                print(" 3 |",end = "")
            elif tab[i][j] == 4:
                print(" 4 |",end = "")
            elif tab[i][j] == 5:
                print(" 5 |",end = "")
            elif tab[i][j] == 6:
                print(" 6 |",end = "")
            elif tab[i][j] == 7:
                print(" 7 |",end = "")
            elif tab[i][j] == 8:
                print(" 8 |",end = "")
            else:
                print(" 9 |",end = "")

            if j == 8:
                print("")
    print("+---+---+---+ +---+---+---+ +---+---+---+")

def check(tab,x,y,v):
    for i in range(9):
        if tab[i][y] == v:
            return 1
    for j in range(9):
        if tab[x][j] == v:
            return 1
    if x < 3:
        if y < 3:
            for i in range(3):
                for j in range(3):
                    if tab[i][j] == v:
                        return 1
        elif y < 6:
            for i in range(3):
                for j in range(3,6):
                    if tab[i][j] == v:
                        return 1
        else:
            for i in range(3):
                for j in range(6,9):
                    if tab[i][j] == v:
                        return 1
    elif x < 6:
        if y < 3:
            for i in range(3,6):
                for j in range(3):
                    if tab[i][j] == v:
                        return 1
        elif y < 6:
            for i in range(3,6):
                for j in range(3,6):
                    if tab[i][j] == v:
                        return 1
        else:
            for i in range(3,6):
                for j in range(6,9):
                    if tab[i][j] == v:
                        return 1
    else:
        if y < 3:
            for i in range(6,9):
                for j in range(3):
                    if tab[i][j] == v:
                        return 1
        elif y < 6:
            for i in range(6,9):
                for j in range(3,6):
                    if tab[i][j] == v:
                        return 1
        else:
            for i in range(6,9):
                for j in range(6,9):
                    if tab[i][j] == v:
                        return 1
    return 0


def play(tab,err):
    x = int(input("Enter the number of the line : "))
    y = int(input("Enter the number of the column : "))
    while(tab[x-1][y-1] != 0 or x < 1 or x > 9 or y < 0 or y > 9):
        if(x < 1 or x > 9 or y < 1 or y > 9):
            print("Cellule doesn't exist")
        else:
            print("That cellule is already filled")
        x = int(input("Enter the number of the line : "))
        y = int(input("Enter the number of the column : "))
    v = int(input("Enter the value : "))

    if check(tab,x-1,y-1,v) != 1:
        tab[x-1][y-1] = v
    
    else:
        print("You made a mistake")
        err = err + 1

    return tab, err

def game_over(tab,err):
    if err == 3:
        print("You made 3 mistakes. You failed")
        return 1
    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                return 0
    print("Sudoku completed. You won")
    draw_table(tab)
    return 1
            

tab =  [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

values = [[[7,1,4,2,5,0,3,8,0],[0,6,0,0,0,0,1,9,0],[5,0,9,6,3,1,7,2,0],[0,0,0,8,0,0,0,0,1],[8,0,5,0,0,0,2,0,0],[4,2,0,0,6,5,0,0,0],[0,4,0,0,0,0,5,0,0],[0,0,7,0,1,8,0,0,2],[0,0,0,5,9,0,6,0,7]],
          [[5,0,0,6,0,7,0,9,0],[1,2,6,0,0,0,0,4,0],[0,9,0,0,2,0,6,0,0],[6,0,0,0,0,0,0,2,4],[9,3,1,0,7,4,0,0,0],[0,4,5,8,3,6,0,7,9],[3,5,0,7,1,0,0,6,0],[0,0,2,0,0,3,8,1,5],[0,0,0,0,0,2,4,0,0]],
          [[0,0,0,0,0,0,3,7,0],[0,0,0,9,0,8,0,0,1],[1,8,5,0,0,3,0,2,0],[5,3,0,0,7,2,9,8,0],[0,4,9,8,0,1,0,5,7],[8,0,0,0,4,9,6,1,3],[7,0,3,0,0,4,0,0,6],[4,9,0,1,0,0,8,0,0],[0,0,0,3,0,6,0,0,0]],
          [[3,0,6,4,5,0,0,0,0],[0,0,0,6,0,0,0,2,0],[1,8,0,0,7,0,0,0,5],[9,1,4,5,0,7,6,0,3],[0,0,0,1,0,3,0,4,0],[6,0,7,9,0,8,5,1,2],[4,6,0,0,0,0,2,7,0],[0,0,8,0,1,0,0,0,0],[0,0,0,7,0,0,8,0,6]],
          [[0,0,0,0,0,0,7,0,6],[0,7,0,9,0,6,3,0,0],[0,5,0,4,7,3,8,9,0],[1,3,2,0,0,5,0,7,9],[0,0,4,2,1,0,5,3,8],[0,9,0,0,0,4,0,0,0],[0,2,7,0,6,8,0,1,3],[0,0,0,0,4,0,0,8,0],[6,0,0,0,9,7,0,0,4]],
          [[0,7,9,3,0,0,0,0,0],[3,0,2,0,0,0,5,0,7],[0,0,0,0,0,1,0,9,0],[5,0,0,1,8,0,0,0,0],[1,2,6,4,9,0,7,3,0],[0,8,7,6,3,0,4,5,1],[0,6,0,0,0,3,1,0,9],[0,0,0,5,0,6,8,7,0],[2,0,0,7,0,0,0,0,0]],
          [[0,5,0,0,0,9,8,1,3],[9,8,0,3,5,0,6,0,7],[6,0,0,0,8,0,5,9,4],[8,3,2,0,0,6,0,0,0],[7,0,0,1,2,8,0,0,9],[1,9,0,0,7,3,2,0,0],[3,7,0,6,9,0,0,5,0],[0,2,0,0,0,0,7,0,0],[0,0,0,0,0,4,0,0,0]],
          [[0,0,0,0,0,1,8,0,2],[7,1,8,6,2,0,9,0,4],[6,4,0,9,3,8,7,0,5],[8,0,5,0,9,0,0,4,0],[2,6,0,0,0,0,1,9,0],[0,0,0,0,0,3,6,0,0],[1,0,6,3,0,4,0,0,0],[0,0,0,5,6,0,4,0,0],[0,5,0,0,0,0,0,8,0]],
          [[0,6,0,0,0,0,5,0,3],[0,8,1,0,0,2,0,0,4],[4,5,0,0,1,6,0,7,0],[2,0,8,0,6,5,3,0,0],[0,7,3,0,2,4,0,5,0],[1,4,0,0,0,0,9,0,0],[0,0,7,0,0,0,0,6,0],[9,0,6,0,4,7,2,8,1],[0,0,4,0,0,1,0,3,5]],
          
          [[4,0,7,0,8,0,0,0,5],[3,0,0,0,0,5,0,0,0],[0,1,5,0,0,6,9,4,0],[0,0,0,0,0,4,0,9,8],[9,0,3,0,0,0,2,0,4],[2,4,0,0,7,9,0,0,0],[0,0,0,6,5,0,8,0,0],[5,8,6,0,0,0,4,2,7],[0,0,0,0,0,0,5,0,0]],
          [[9,0,4,0,1,0,6,7,0],[0,0,7,0,9,0,8,3,0],[0,0,0,0,0,8,0,0,9],[0,0,0,0,0,0,0,0,5],[0,0,0,8,0,0,7,0,3],[5,0,1,7,0,0,9,2,0],[0,0,0,9,0,4,1,5,0],[7,0,0,0,8,2,0,9,0],[1,0,6,0,0,0,0,0,0]],
          [[0,3,0,0,0,5,4,7,0],[0,0,0,0,0,4,0,6,0],[7,0,0,0,0,0,0,3,0],[0,0,0,2,0,6,0,4,0],[0,4,9,0,8,1,7,2,0],[2,5,0,0,4,0,8,0,0],[4,0,0,0,0,8,9,1,0],[0,1,0,0,3,0,6,0,0],[0,8,3,0,0,0,0,0,0]],
          [[8,2,0,0,1,5,0,0,0],[0,1,5,0,0,0,2,4,0],[0,0,0,2,0,9,5,0,0],[0,0,0,0,9,0,0,3,6],[6,3,9,1,5,4,0,0,0],[0,0,0,0,3,0,0,0,0],[4,5,0,0,0,3,0,9,0],[3,0,7,5,2,0,6,0,0],[0,8,0,0,0,0,3,0,0]],
          [[2,0,0,0,0,1,0,0,0],[0,0,0,0,4,0,0,1,0],[1,5,0,2,0,8,4,0,0],[0,7,0,0,0,9,0,0,0],[0,3,1,0,5,0,6,0,0],[0,4,0,3,1,0,0,2,0],[4,0,0,8,0,0,9,6,0],[0,0,3,9,0,0,1,0,0],[0,2,0,0,6,5,3,0,0]],
          [[0,0,0,0,0,2,5,3,0],[6,1,0,0,0,0,0,2,0],[0,0,0,3,0,0,6,4,9],[0,0,0,0,0,7,0,0,0],[0,4,5,0,0,0,0,1,8],[0,9,6,8,2,0,0,0,3],[3,0,0,0,4,5,0,6,0],[4,0,0,6,7,0,0,0,0],[0,0,1,0,9,0,0,0,4]],
          [[0,0,6,0,7,0,1,0,5],[0,5,0,4,0,9,0,0,0],[0,0,0,0,0,0,2,0,8],[4,6,9,8,0,0,5,1,0],[0,0,1,0,4,0,0,3,6],[7,0,5,0,9,0,8,0,0],[0,0,4,0,0,0,0,0,0],[0,0,0,9,0,0,0,6,0],[8,0,0,6,0,3,4,0,0]],
          [[3,0,0,0,0,0,0,0,8],[0,0,7,8,3,0,0,0,0],[0,0,0,1,9,0,0,0,3],[0,0,5,0,0,0,9,0,0],[0,6,3,4,0,0,0,0,5],[0,0,0,5,0,0,0,7,4],[8,0,0,0,0,0,6,4,9],[5,0,9,0,1,3,0,2,0],[6,0,2,0,1,3,0,2,0]],
          [[0,4,0,0,0,1,0,0,0],[5,0,0,0,4,0,0,1,3],[1,0,6,8,0,7,0,0,0],[0,6,1,0,5,3,0,0,0],[0,0,0,2,0,0,0,6,9],[3,0,8,0,9,0,0,7,0],[2,0,0,0,0,0,7,0,0],[7,0,3,9,0,0,4,5,1],[0,0,0,0,0,4,0,0,0]],
          
          [[0,0,7,0,0,1,2,0,0],[0,0,9,4,0,0,8,0,7],[0,0,8,0,0,5,0,0,0],[0,0,0,0,0,0,0,0,0],[1,0,0,0,0,4,7,0,0],[0,0,2,0,9,0,6,0,0],[2,0,0,5,0,0,0,6,0],[0,0,0,0,0,0,0,8,5],[3,0,0,0,0,6,4,0,0]],
          [[0,0,0,0,0,0,3,0,2],[0,0,0,3,0,6,1,0,0],[9,0,3,0,0,0,5,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,7,0,0,9],[1,6,2,8,9,0,0,0,4],[8,0,0,0,5,0,0,0,0],[7,0,0,0,0,3,0,0,1],[3,4,5,0,7,0,0,0,0]],
          [[0,0,5,2,0,0,8,0,0],[8,9,1,0,0,3,2,0,0],[0,0,0,0,0,0,0,0,9],[1,0,2,0,0,0,0,0,0],[0,7,9,8,0,0,1,0,2],[0,0,0,0,0,9,0,0,0],[0,0,0,0,5,0,4,0,7],[0,0,7,0,3,0,9,1,5],[2,0,0,0,1,0,0,0,3]],
          [[0,0,7,0,0,0,0,0,5],[5,0,0,4,2,0,0,0,1],[0,4,0,0,0,5,6,0,0],[6,0,5,1,0,0,0,0,0],[0,0,0,0,0,8,0,0,0],[2,0,0,0,0,0,0,8,0],[9,2,0,0,7,0,0,5,0],[0,7,3,0,0,6,0,0,0],[0,0,1,0,0,9,0,0,2]],
          [[0,0,3,0,0,1,0,0,2],[0,0,9,0,5,0,0,1,0],[0,0,0,0,0,0,5,8,0],[0,0,0,0,0,0,0,0,0],[0,0,6,0,0,2,0,0,7],[9,0,0,4,0,0,0,0,1],[4,0,0,0,2,0,7,0,8],[8,0,0,0,0,5,0,0,0],[7,0,0,0,0,6,0,0,9]],
          [[5,0,8,7,4,0,0,0,3],[0,0,2,0,9,1,0,0,0],[0,9,0,0,6,8,0,0,0],[0,0,0,0,0,4,7,0,0],[0,0,0,6,0,0,0,0,0],[9,2,6,0,8,0,0,4,0],[2,0,0,0,0,0,0,3,0],[7,0,4,0,0,0,1,0,2],[0,8,5,0,0,0,0,0,9]],
          [[9,0,5,4,0,0,6,0,7],[0,0,0,9,0,7,0,0,0],[4,2,0,0,0,0,9,1,0],[5,0,8,0,0,0,0,0,0],[0,0,0,0,6,5,0,0,0],[0,0,0,1,0,9,0,0,0],[0,0,6,0,0,3,8,0,0],[0,0,0,0,8,0,0,2,6],[8,0,0,2,0,6,3,4,0]],
          [[0,1,0,0,0,0,0,0,0],[6,9,0,0,2,0,0,5,7],[0,0,0,0,6,9,2,0,0],[0,0,9,0,0,0,4,0,0],[4,7,0,0,0,0,0,2,0],[5,8,1,0,9,0,0,0,3],[0,0,5,0,0,8,6,0,0],[0,4,0,2,0,0,8,0,1],[0,0,0,6,0,0,0,4,0]],
          [[0,8,0,0,0,0,0,0,3],[0,6,0,0,7,0,4,0,5],[3,0,4,0,6,1,0,0,0],[5,0,0,9,0,0,6,0,2],[0,0,0,0,0,0,0,3,1],[0,0,7,0,0,0,0,0,0],[0,0,0,1,0,6,2,0,0],[2,0,8,0,4,5,0,0,6],[0,0,6,0,0,0,0,5,7]],
          
          [[9,1,0,0,0,7,0,0,0],[0,0,7,0,1,3,0,0,8],[6,0,0,0,0,4,0,0,0],[0,0,2,0,0,0,0,8,0],[0,0,0,0,0,0,7,3,4],[0,0,0,5,0,0,0,1,0],[3,4,0,0,2,0,0,0,0],[0,0,0,0,0,0,9,0,6],[0,0,0,8,0,0,0,7,0]],
          [[0,3,0,0,0,0,0,0,2],[6,4,0,0,7,0,0,0,0],[8,0,0,0,0,0,5,0,9],[0,0,0,9,6,0,0,0,0],[0,9,0,0,0,8,0,0,7],[0,0,0,0,0,0,3,0,0],[0,0,2,0,0,0,0,0,5],[1,0,5,0,0,4,7,0,0],[0,0,0,6,1,0,0,0,0]],
          [[0,0,9,2,0,8,7,0,0],[7,0,0,0,0,0,0,3,0],[0,2,0,0,0,0,1,0,0],[0,4,1,0,0,2,0,0,0],[0,0,6,1,0,0,0,0,0],[0,0,0,3,0,0,5,6,0],[9,0,0,0,0,0,0,0,3],[0,0,0,6,4,0,0,0,0],[2,0,0,0,0,0,9,8,0]],
          [[0,0,0,0,4,0,0,2,6],[3,0,9,7,2,0,0,0,0],[0,5,0,0,0,0,4,0,0],[0,0,7,9,1,3,0,0,0],[6,0,3,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2],[1,0,0,0,0,0,0,8,0],[0,0,0,0,0,8,0,0,9],[0,9,0,0,0,0,7,0,4]],
          [[0,0,0,0,0,5,4,0,6],[0,0,0,0,0,0,0,0,0],[0,0,0,2,0,8,0,5,0],[0,1,3,0,9,0,8,0,7],[0,0,4,0,0,0,0,0,1],[0,0,0,8,0,0,0,0,9],[0,0,8,0,0,1,9,0,0],[0,2,0,7,3,0,0,0,0],[5,0,0,0,0,0,0,7,0]],
          [[0,6,1,0,0,5,0,0,0],[0,0,0,0,0,4,0,2,0],[0,0,0,0,9,0,0,0,6],[0,0,0,0,0,0,8,7,2],[5,0,9,0,0,0,4,0,0],[0,0,3,0,0,0,9,0,0],[7,0,0,0,0,0,0,0,0],[8,0,0,2,0,0,0,0,4],[0,9,0,8,7,0,0,0,0]],
          [[0,8,0,0,6,0,0,0,1],[0,0,7,0,0,1,0,0,0],[6,0,0,4,0,9,0,8,7],[0,0,0,0,0,0,9,4,0],[0,4,5,0,0,0,0,0,8],[0,0,0,0,0,0,5,0,0],[3,0,0,0,0,0,0,9,0],[4,2,0,0,0,0,0,0,0],[0,0,1,2,0,0,7,0,0]],
          [[0,1,0,0,8,6,0,0,7],[0,0,0,0,0,4,9,0,5],[0,0,0,1,0,0,0,0,0],[0,7,0,0,5,0,0,3,2],[0,0,0,0,0,0,0,0,0],[0,0,0,0,9,0,7,0,0],[0,0,6,0,1,0,0,0,9],[3,4,0,0,0,0,0,0,1],[8,0,0,0,3,0,0,5,0]],
          [[9,0,0,0,0,0,0,0,4],[3,0,0,5,6,0,0,0,0],[0,8,0,0,0,0,5,0,0],[0,0,4,0,0,1,9,0,0],[0,0,0,0,0,7,0,0,0],[0,7,1,8,0,0,0,0,0],[0,0,0,0,0,0,4,1,7],[0,0,0,0,2,0,0,8,0],[0,0,0,0,8,3,0,9,0]]]

err = 0
gameOver = 0

print("[0: Easy] [1: Medium] [2: Hard] [3: Expert]")
Diff = int(input("Choose a dificulty : "))
while(Diff < 0 or Diff > 3):
    print("You have to choose one of the available difficulties")
    print("[0: Easy] [1: Medium] [2: Hard] [3: Expert]")
    Diff = int(input("Choose a difficulty : "))

if Diff == 0:
    r = random.randint(0,8)
elif Diff == 1:
    r = random.randint(9,17)
elif Diff == 2:
    r = random.randint(18,26)
else:
    r = random.randint(27,35)

initialize_table(tab,values[r])
print("Game Started")

while(gameOver != 1):
    draw_table(tab)
    tab, err = play(tab,err)
    gameOver = game_over(tab,err)
    print("")
    print("Number of mistakes ",err)
""
