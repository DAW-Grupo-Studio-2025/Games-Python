def DisplayBoard(board):
    for i in board: 
        print(*i)
    

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    listOfFreeFields = []
    n = 1
    for fila in board: 
        
        for columna in fila: 
            if columna == "-":
                listOfFreeFields.append(n)
            n += 1

    return listOfFreeFields


def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
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
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    user_enter = int(input("Enter free number of the field from 1 to 9: "))
    if user_enter not in MakeListOfFreeFields(board):
        print("This field is ocupied")
    else: 
        board[(user_enter-1)//n][(user_enter-1)%n] = "o"

    return board 

    """elif user_enter == 1: 
        board[0][0] = "o"
    elif user_enter == 2 : 
        board[0][1] = "o"
    elif user_enter == 3: 
        board[0][2] = "o"
    elif user_enter == 4 : 
        board[1][0] = "o"
    elif user_enter == 5: 
        board[1][1] = "o"
    elif user_enter == 6: 
        board[1][2] = "o"
    elif user_enter == 7: 
        board[2][0] = "o"
    elif user_enter == 8: 
        board[2][1] = "o"
    elif user_enter == 9: 
        board[2][2] = "o"""

    




"""def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

    
    user_enter = int(input("Enter free number of the field from 1 to 9: "))
    if user_enter in range(9): 
        if user_enter == 1 and board[0][0] !=1: 
            board[0][0] = "o"
        elif user_enter == 2 and board[0][1] !=1: 
            board[0][1] = "o"
        elif user_enter == 3 and board[0][2] !=1: 
            board[0][2] = "o"
        elif user_enter == 4 and board[1][0] !=1: 
            board[1][0] = "o"
        elif user_enter == 5 and board[1][1] !=1: 
            board[1][1] = "o"
        elif user_enter == 6 and board[1][2] !=1: 
            board[1][2] = "o"
        elif user_enter == 7 and board[2][0] !=1: 
            board[2][0] = "o"
        elif user_enter == 8 and board[2][1] !=1: 
            board[2][1] = "o"
        elif user_enter == 9 and board[2][2] !=1: 
            board[2][2] = "o"

    
    return board

    
"""

            

def VictoryFor(board):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
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


#primera columna
    if board[0][0] != "-" and board[0][0] == board[1][0] and board[1][0] == board[2][0]: 
        if board[0][0] == "x":
            victoryX = True
        if  board[0][0] == "o": 
            victoryO = True
#diagonal
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

#segunda columna 
    if board[0][1] != "-" and board[0][1] == board[1][1] and board[1][1] == board[2][1]: 
        if board[0][1] == "x":
            victoryX = True
        if  board[0][1] == "o": 
            victoryO = True

#tercera columna 
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

    

    








board = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

DisplayBoard(board)
print("""Computer goes with 'x' and user goes with 'o'\n 
      Computer starts first""")
board[1][1] = "x"
DisplayBoard(board)
while not VictoryFor(board):
    
    
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board): 
        
        break 
    DrawMove(board)
    DisplayBoard(board)
    
    
        






