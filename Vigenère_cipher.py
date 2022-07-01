#THIS CODE IS AN EASY IMPLEMENTATION OF THE VIGENÈRE CIPHER.
#If you do not know how the Vigenère cipher works check out the description given by Wikipedia(I found it very helpful):https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
def vigenere2(s, k):#This is our function where our Vigenère cipher implementation take part. Two parameters are taken.
    my_alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'#My string where the alphabet in use is stored.
    cifrado = []#I will make use of this list to store the letters whose position are the result of the sum of the index position
#that each letter of my_string have in the alphabet and the index position that each letter of the key have in the alphabet. 
    x = 0#This variable will work as a count.
    y = 0#This variable will work as a count too.
    while x < len(s) and y < len(k):
        cifrado.append(my_alphabet[((my_alphabet.index(s[x])) + my_alphabet.index(k[y])) % 27])#We are appending
#the letters whose index position is the result of the sum between the index position that each letter of the my_string have 
#in the alphabet and the index position that each letter of the key have in the alphabet. 
#We use %27 because each time that we pass through 27 we need to start from 0. For more information
#about modular arithmetic:https://en.wikipedia.org/wiki/Modular_arithmetic.
        x += 1
        y = (y + 1) % len(k)#Here we are using %len(k) once again because each time we passed through the length of
#k we need to start from 0.
    print("".join(cifrado))#We join all the letters in the list called "cifrado". And we get our encrypted string.

if __name__ == '__main__':
    my_string = input().upper()#We are making all the letters uppercase. This is just a preference.
    llave = input().upper()#In this case the key is a set of letters. In our function we are going to take the index
#position that each letter of the key has in the alphabet.
    vigenere2(my_string, llave)
