let my_alphabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let cifrado = [];
let s = "rafaz".toLocaleUpperCase();
let k = 0

function CaesarCipher(s, k) {
    for (let i = 0; i < s.length; i++) {
        cifrado.push(my_alphabeto[(my_alphabeto.indexOf(s[i]) + k) %26]);
    }console.log(cifrado);
}
CaesarCipher(s, k);
