let matrix = [[1, 0, 2], [0, 1, 3], [5, 4, 6]]
let suma_principal = 0
let suma_secundaria = 0
for (let i = 0; i < matrix.length; i++) {
    suma_principal += matrix[i][i]
}
for (let i = 0; i < matrix.length; i ++){
    suma_secundaria += matrix[i][matrix.length - 1 - i]
}

console.log(suma_principal)
console.log(suma_secundaria)
