let my_array = [9, 7, 1, 2, 5, 4, 8, 0]
let swap = true
let comparaciones_necesarias = my_array.length - 1
function bubblesort(arr) {
    while (swap === true && comparaciones_necesarias > 0)
    {
        swap = false
        for (let i = 0; i <= comparaciones_necesarias; i++){
            if (my_array[i] > my_array[i + 1]){
                [my_array[i], my_array[i + 1]] = [my_array[i + 1], my_array[i]]
                swap = true
            }
        }
        comparaciones_necesarias -= 1
        
    }
    return arr
}
console.log(bubblesort(my_array));
