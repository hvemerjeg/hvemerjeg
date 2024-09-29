# THIS CODE IS AN EASY IMPLEMENTATION OF THE VIGENERE CIPHER
import sys
import operator
class VigenereCipher:
    alphabet = [chr(num) for num in range(ord('A'), ord('Z') + 1)]
	# encrypt and decrypt function
    def encrypt_decrypt(string: str, key: str) -> str:
        if sys.argv[1] == 'enc':
            operation = operator.add
        elif sys.argv[1] == 'dec':
            operation = operator.sub
        result = ''
        for indx in range(len(string)):
            if string[indx] not in VigenereCipher.alphabet:
                result += string[indx]
            else:
                result += VigenereCipher.alphabet[operation(VigenereCipher.alphabet.index(string[indx]), VigenereCipher.alphabet.index(key[indx % len(key)])) % len(VigenereCipher.alphabet)]
        return result

def main() -> None:
    '''
    python3 Vigenere_cipher.py enc
    python3 Vigenere_cipher.py dec
    '''
    if len(sys.argv) != 2:
        sys.stderr.write(f'[ + ] Usage: {sys.argv[0]} enc/dec\n')
        exit(1)
    if sys.argv[1] == 'enc':
        plaintext = input('Insert message to encrypt: ').upper()
        key = input('Insert key: ')
        ciphertext = VigenereCipher.encrypt_decrypt(plaintext, key)
        print(f'Ciphertext: {ciphertext}')
    elif sys.argv[1] == 'dec':
        ciphertext = input('Insert message to decrypt: ').upper()
        key = input('Insert key: ')
        plaintext = VigenereCipher.encrypt_decrypt(ciphertext, key)
        print(f'Plaintext: {plaintext}')
if __name__ == '__main__':
    main()
