def DisplayBoard(board):
    for i in board: 
        print(*i)
    

def MakeListOfFreeFields(board):
    listOfFreeFields = []
    n = 1
    for fila in board: 
        
        for columna in fila: 
            if columna == "-":
                listOfFreeFields.append(n)
            n += 1

    return listOfFreeFields


def DrawMove(board):
    print("Computers turn")
    step = False
    for fila in board: 
        for i in range(3): 
            if fila[i] == "-": 
                fila[i] = "x"
                step = True
                break
        if step: 
            break   

    return board
             

def EnterMove(board):
    n = 3
    user_enter = int(input("Enter free number of the field from 1 to 9: "))
    if user_enter not in MakeListOfFreeFields(board):
        print("This field is ocupied")
    else: 
        board[(user_enter-1)//n][(user_enter-1)%n] = "o"

    return board 

            

def VictoryFor(board):
    victoryX = False 
    victoryO = False

    if board[0][0] != "-" and board[0][0] == board[0][1] and board[0][1] == board[0][2]: 
        if board[0][0] == "x":
            victoryX = True
        if  board[0][0] == "o": 
            victoryO = True

    if board[1][0] != "-" and board[1][0] == board[1][1] and board[1][1] == board[1][2]: 
        if board[1][0] == "x":
            victoryX = True
        if  board[1][0] == "o": 
            victoryO = True

    if board[2][0] != "-" and board[2][0] == board[2][1] and board[2][1] == board[2][2]: 
        if board[2][0] == "x":
            victoryX = True
        if  board[2][0] == "o": 
            victoryO = True


    if board[0][0] != "-" and board[0][0] == board[1][0] and board[1][0] == board[2][0]: 
        if board[0][0] == "x":
            victoryX = True
        if  board[0][0] == "o": 
            victoryO = True

    if board[0][0] != "-" and board[0][0] == board[1][1] and board[1][1] == board[2][2]: 
        if board[0][0] == "x":
            victoryX = True
        if  board[0][0] == "o": 
            victoryO = True

    if board[0][2] != "-" and board[0][2] == board[1][1] and board[1][1] == board[2][0]: 
        if board[1][1] == "x":
            victoryX = True
        if  board[1][1] == "o": 
            victoryO = True

    if board[0][1] != "-" and board[0][1] == board[1][1] and board[1][1] == board[2][1]: 
        if board[0][1] == "x":
            victoryX = True
        if  board[0][1] == "o": 
            victoryO = True

    if board[0][2] != "-" and board[0][2] == board[1][2] and board[1][2] == board[2][2]: 
        if board[0][2] == "x":
            victoryX = True
        if  board[0][2] == "o": 
            victoryO = True
    
    if victoryX: 
        print("Fail. Computer wins!")
        return victoryX
    elif victoryO: 
        print("You win!")
        return victoryO

    
def main():
    board = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

    DisplayBoard(board)
    print("""Computer goes with 'x' and user goes with 'o'\n Computer starts first""")
    board[1][1] = "x"
    DisplayBoard(board)
    while not VictoryFor(board):
    
    
        EnterMove(board)
        DisplayBoard(board)
        if VictoryFor(board): 
        
            break 
        DrawMove(board)
        DisplayBoard(board)
    
if __name__=="__main__":
    main()






