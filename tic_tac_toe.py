#THIS CODE IS AN EASY IMPLEMENTATION OF THE GAME TIC TAC TOE. IT IS AN EXERCISE THAT APpEARS ON THE STUDY RESOURCES OF THE PCEP.
#I THINK THAT THIS CODE MIGHT BE USEFUL FOR SOME PEOPLE.
def lanzar_juego(player1: str, player2: str):#This function will perform a greeting.
    print(f"\nHi {player1} and {player2}")#Using kind of the new school of python formatting we print our greetings with the variables player1 and player2.
    print("""
+================================+
| Welcome to \"Tres en raya\"      |
| game made by Rafael José.      |
|     Play and enjoy the game.   |
|                                |
+================================+""")

def display_board():#BOARD DRAW.
    print("+" + "-" * 30 + "+")
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|")) 
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print(("|" + " " * 4 + a + " " * 4 + "|" + " " + " " * 3 + b + " " * 4 + "|" + " " * 5 + c + " " * 4 + "|"))
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print("+" + "-" * 30 + "+")
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|")) 
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print(("|" + " " * 4 + d + " " * 4 + "|" + " " + " " * 3 + e + " " * 4 + "|" + " " * 5 + f + " " * 4 + "|"))
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print("+" + "-" * 30 + "+")
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|")) 
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print(("|" + " " * 4 + g + " " * 4 + "|" + " " + " " * 3 + h + " " * 4 + "|" + " " * 5 + i + " " * 4 + "|"))
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print(("|" + " " * 9 + "|" + " " * 9 + "|" + " " * 10 + "|"))
    print("+" + "-" * 30 + "+")

player1 = input("Por favor introduce el nombre del jugador 1: ")
player2 = input("Por favor introduce el nombre del jugador 2: ")
lanzar_juego(player1, player2)
dimensions_board = [[None for i in range(3)] for j in range (3)]#A Tic Tac Toe board is a matrix, so we are creating one matrix full of None values(It is 
#possible to work without a matrix and instead use a list of length nine and that would be easier. Keep in mind that normally there are several ways of solving the same problem
#and this code is just one way).
#I fullfill this nested list(matrix) with None values because I think that it is easier to interact with the data. We are going to change 
#the None values with "X" or "O", so if a position has a value different than None we know that the position
#is already occupied since all the posibles positions were fullfilled with None values at the beginning.
a, b, c, d, e, f, g, h, i = "1", "2", "3", "4", "5", "6", "7", "8", "9"#This variables stores the numbers that are displayed on the board.
display_board()#We call the function to display the board, so the user can see which positions correspond to wich number.
contador = 1#This is a variable that I will use to know when the game is done, because the game only has nine positions, so nine possible moves.
play = 1#One represents the first player(player1), two represents the second player(player2). We are going to use the module(%) operator to
#create turns.
diccionario_moves = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}#With the use of a dictionary
#we are making relations between the positions(1, 2, 3...9) and the "real" position. If we made use of a list of length nine instead of a nested list(matrix) this 
#variable needs to be affected too.

while contador < 10:#Since we only have nine moves, nine turns. We are playing a maximum of nine moves.
    
    if play % 2 != 0:
        player = 1
        move = int(input(f"{player1}'s MOVE: "))
    else:
        player = 2
        move = int(input(f"{player2}'s MOVE: "))
    if player == 1:
        if dimensions_board[diccionario_moves[move][0]][diccionario_moves[move][1]] == None:
            dimensions_board[diccionario_moves[move][0]][diccionario_moves[move][1]] = "X"
            if move == 1:
                a = "X"
            elif move == 2:
                b = "X"
            elif move == 3:           
                c = "X"
            elif move == 4:
                d = "X"
            elif move == 5:
                e = "X"
            elif move == 6:
                f = "X"
            elif move == 7:
                g = "X"
            elif move == 8:
                h = "X"
            elif move == 9:
                i = "X"
        else:
            print(f"The position {move} is already busy")
            continue
    else:
        if dimensions_board[diccionario_moves[move][0]][diccionario_moves[move][1]] == None:
            dimensions_board[diccionario_moves[move][0]][diccionario_moves[move][1]] = "O"
            if move == 1:
                a = "O"
            elif move == 2:
                b = "O"
            elif move == 3:           
                c = "O"
            elif move == 4:
                d = "O"
            elif move == 5:
                e = "O"
            elif move == 6:
                f = "O"
            elif move == 7:
                g = "O"
            elif move == 8:
                h = "O"
            elif move == 9:
                i = "O"
        else:
            print(f"The position {move} is already busy")
            continue

    posiciones_ganadoras = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2],\
[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 0], [1, 1], [2, 2], [0, 2], [1, 1], \
[2, 0]]#Here we are storing the different combinations of positions to check if a player has won. If a player has occupied the position (0,0 and 0,1 and 0,2) or 
#(1,0 and 1,1 and 1,2) or (2,0 and 2,1 and 2,2) or etc.. is a win. So to check this we are going to use the % operation and if our counter gets to three
#that means that a player has won. If we iterate through three elements of this nested list and we do not have a win by a player we restart the count. We 
#repeat this process until the end of the nested list posiciones_ganadoras
    contador_player_1 = 0
    contador_player_2 = 0
    reseteo_1 = 1
    reseteo_2 = 1
    if contador == 5 or contador == 7 or contador == 9:#We are going to check if the player1 has won in turns 5, 7, and 9
        for y in posiciones_ganadoras:
            if dimensions_board[y[0]][y[1]] == "X":
                contador_player_1 += 1
                if contador_player_1 == 3:
                    print(f"El jugador {player1} ha ganado")
                    display_board()
                    exit()
            if reseteo_1 % 3 == 0:#If we iterated through three elements and we do not have a victory by the player1 we need to restart the contador_player_1
                contador_player_1 = 0
                reseteo_1 = 1
                continue#We use the continue to go to the beginning of the loop.
            reseteo_1 += 1
    if contador == 6 or contador == 8:#We are going to check if the player 2 has won in turns 6 and 8
        for y in posiciones_ganadoras:
            if dimensions_board[y[0]][y[1]] == "O":
                contador_player_2 += 1
                if contador_player_2 == 3:
                    print(f"El jugador {player2} ha ganado")
                    display_board()
                    exit()
            if reseteo_2 % 3 == 0:#If we iterated through three elements and we do not have a victory by the player2 we need to restart the contador_player_2
                contador_player_2 = 0
                reseteo_2 = 1
                continue
            reseteo_2 += 1
    contador += 1
    play += 1
    display_board()
print("DRAW")
