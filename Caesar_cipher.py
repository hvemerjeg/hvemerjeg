#THIS CODE IS AN EASY IMPLEMENTATION OF THE CAESAR CIPHER
#If you do not know how the caesar cipher works check out the description given by Wikipedia(I found it very helpful):https://en.wikipedia.org/wiki/Caesar_cipher:
def my_cifrado_caesar_2(string, llave):
    my_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'#My string where the alphabet in use is stored.
    indice = []#I will make use of this empty list to store the index that each letter has in the alphabet(my_alphabet).
    cifrado = []#I will use this empty list to store the index that each letter has in the alphabet + the key, so we get the permutation.
    for letter in string:#We iterate through the string and store the index that each letter has in the alphabet in the list(indice).
        indice.append(my_alphabet.index(letter))
    for i in indice:#We make the permutation adding the value of the key to the index that each letter has in the alphabet.
            cifrado.append(my_alphabet[(i + llave) % 26])#We make use the modulus 26 becasue each time that we pass through 26 we need to start from 0. For more information
            #about modular arithmetic:https://en.wikipedia.org/wiki/Modular_arithmetic.
    print("".join(cifrado))#We join all the letters in the list called "cifrado". And we get our encrypted string.
if __name__ == '__main__':
    my_string = input().upper()#We are making all the letters uppercase. This is just a preference.
    llave = int(input())#The key defines how many steps to the right we are going to take to perform the encryption of our letters.
    my_cifrado_caesar_2(my_string, llave)#We call the function.
#This implementation of the Caesar cipher is not a very fancy one, but enough to show the fundamentals of the Caesar cipher and interesting concepts as modular arithmetic.
