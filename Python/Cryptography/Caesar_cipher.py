#THIS CODE IS AN EASY IMPLEMENTATION OF THE CAESAR CIPHER
#If you do not know how the Caesar cipher works check out the description given by Wikipedia(I found it very helpful):https://en.wikipedia.org/wiki/Caesar_cipher
import sys
class CaesarCipher:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'# You can create this with the following bash command: for char in {A..Z}; do echo $char; done | xargs | tr -d ' ' 

    def encrypt(plaintext: str, key: int) -> str:
        ciphertext = ''
        for char in plaintext:
            if char not in CaesarCipher.alphabet:
                ciphertext += char
            else: 
                ciphertext += CaesarCipher.alphabet[(CaesarCipher.alphabet.index(char) + key) % len(CaesarCipher.alphabet)]
        return ciphertext

        
    def decrypt(ciphtext: str, key: int) -> str:
        return CaesarCipher.encrypt(ciphtext, -key)

def main():
    if len(sys.argv) != 2:
        '''
        python3 Caesar_cipher.py enc
        python3 Caesar_cipher dec
        '''
        sys.stderr.write(f'[ + ] Usage: {sys.argv[0]} enc/dec\n')
        exit(1)
    if sys.argv[1] == 'enc':
        plaintext = input('Insert message to encrypt: ').upper()
        key = int(input('Insert key: '))
        ciphertext = CaesarCipher.encrypt(plaintext, key)
        print(f'Ciphertext: {ciphertext}')
    elif sys.argv[1] == 'dec':
        ciphertext = input('Insert message to decrypt: ').upper()
        key = int(input('Insert key: '))
        plaintext = CaesarCipher.decrypt(ciphertext, key)
        print(f'Plaintext: {plaintext}')

if __name__ == '__main__':
    main()
