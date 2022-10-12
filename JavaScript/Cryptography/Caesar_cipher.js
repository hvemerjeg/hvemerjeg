function caesarCipher(plain_text, key) {
    plain_text = plain_text.toUpperCase();
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text = ''
    for (let i = 0; i < plain_text.length; i++) {
        cipher_text += alphabet[(alphabet.indexOf(plain_text[i]) + key) % alphabet.length]
    }
    return cipher_text
}
