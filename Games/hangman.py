#THIS IS AN EASY IMPLEMENTATION OF THE HANGMAN GAME.
#I THINK THAT THIS CODE WILL BE HELPFUL FOR SOME PEOPLE.
import maskpass#We are going to make use of this module to hide the user input when the player is introducing the word to be guessed.
##HANGMAN
def display_scenario(escenario_palabra: list):#This function is to display part of the visual.
    print("\n" + "-"*30 + "*" + " "*20, end=" ")
    print(*escenario_palabra)#The asterisk is to unpack the list escenario_palabra.
    print(" "*30 + "|")

def display_hangman(parte: str):#This one is to display parts of the hangman when the player fails a guess.
    a = (" "*30 + "O")
    b = (" "*29 + "-")
    c = ("|")
    d = ("-")
    e = ( " "*29 + "/")
    f = (" \\")

    if parte == "a":
        print(a)
    elif parte == "b":
        print(b, end="")
    elif parte == "c":
        print(c, end="")
    elif parte == "d":
        print(d)
    elif parte == "e":
        print(e, end="")
    elif parte == "f":
        print(f, end="")

def presentación(player1: str, player2: str):#This is a function to perform the greeting.
    print(f"\nHi {player1} and {player2}")#Using kind of the new school of python formatting we print our greetings with the variables player1 and player2.
    print("""
+================================+
| Welcome to \"Hangman\"           |
| game made by Rafael José.      |
|     Play and enjoy the game.   |
|                                |
+================================+""" + "\n\n\n")

def dinámica(jugador_activo: str):#This function stores the game.
    ##SET UP
    letras_repetidas = []
    partes_lista = ["a", "b", "c", "d", "e", "f"]
    partes = ""#Here we are going to store the parts of the hangman to be displayed.
    palabra = maskpass.askpass(f"{jugador_activo} introduce palabra: ", mask="*").upper()#Here we are using the function askpass of the module maskpass to hide the word to be guessed.
    palabra_escenario = []#The following is to display the spaces representing the number of letters that the word to be guessed has.
    for i in range(len(palabra)):
        palabra_escenario.append("_") 
    display_scenario(palabra_escenario)


    ##PLAYING
    aciertos = 0#We are going to store the number of hits, to determine if the player2 has won.
    jugadas = 0#This will be useful to store which position of the variable partes_lista needs to be appended to the variable partes.
    while len(partes) < 6:#Because the hangman(in this case) consists of 6 parts. The game is not finished until the hangmans is completed or the player2 guessed the whole word.
        adivina_letra = input(f"\n{jugador2} INTRODUCE LETRA: ").upper()
        if adivina_letra in letras_repetidas:#If the letter is already in the list letras_repetidas, we are going to ask for another letter.
            print(f"Esa letra ya la has dicho!!\nPrueba con otra")
            continue
        letras_repetidas.append(adivina_letra)#We are appending the letter that has been introduced if is not in the list already.
        numero_de_aciertos = 0#We will use this variable to determine if a part of the hangman needs to be added to the variable parts. 
#In case that there is no hits by the player2, numero de aciertos 
#equals zero. Otherwise numero de aciertos > 0.
        for i in range(len(palabra)):
            if palabra[i] == adivina_letra:
                palabra_escenario[i] = adivina_letra
                aciertos += 1
                numero_de_aciertos += 1
            elif numero_de_aciertos < 1 and i == (len(palabra) - 1):
                partes += partes_lista[jugadas]
                jugadas += 1
        display_scenario(palabra_escenario)
        for i in partes:
            display_hangman(i)
        if aciertos == len(palabra):#If the number of hits is equal to the length of the word introduced to be guessed then the player2 has won.
            print(f"\n{jugador2} WINS!!")
            exit()
    print(f"\n{jugador1} WINS!!\nLa palabra era {palabra}")#If we get outside the while loop that means len(partes) == 6, so the whole hangman has been displayed already.

if __name__ == '__main__':
    jugador1 = input("Introduce el nombre del jugador 1(es decir, el que pone palabra): ").capitalize()
    jugador2 = input("Introuduce el nombre del jugador 2(es decir, el que adivina letras): ").capitalize()
    presentación(jugador1, jugador2)
    dinámica(jugador1)
