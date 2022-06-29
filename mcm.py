#THIS CODE IS AN EASY IMPLEMENTATION MCM CALCULATOR
import numpy#We will need the numpy function .prod() to compute the product of all the elemenets inside a list.
def mcm(arr):#This is our function that will hold the code to find the mcm of n numbers.
    lista_de_listas = [[] for i in arr]#With lists comprehesion we are going to create a list that contains differents lists(nested list). The numbers of lists 
#inside the list will depend on the number of numbers whose we want to find the mcm.
    for i in arr:#This loop will do the following:
        h = 2#To find the mcm of n numbers first of all we need to decompose into prime factors. The first prime factor is 2, that is the reason why h queals to 2.
        while i > 1:#We know when we are done in our factor decomposition when the number is equals to 1
            if i % h == 0:#If the number we want to decompose is divisible by 2 we start our decomposition with 2. Otherwise we increase by one since the distribution
#of the prime numbers is a real problem for real mathematicians...
                lista_de_listas[arr.index(i)].append(h)#We append h to lista_de_listas at the same index that i has in arr.
                arr.insert(arr.index(i), (int(i / h)))
                arr.remove(i)#The last two lines is a way to update the value of i. First of all we insert at index(i) the result of i / h and the we delete i.
                i = int(i / h)#We update the value of i to i / h
            else:
                h += 1
    """COGIENDO LOS COMUNES Y NO COMUNES ELEVADOS A SU MÁXIMO EXPONENTE"""
    pseudo_todos = list(map(set, lista_de_listas))#We make take our list of lists and convert the lists inside this list to sets and we store this in this pseudo_todos
#variable.
    todos = set()#We create a new empty set where we are going to store all the prime factors
    for i in pseudo_todos:#This loop is for store all the prime factors in todos.
        for x in i:
            todos.add(x)
    my_dictionario_todos = {i: 0 for i in todos}#As we did before with lists comprehension, we create a dictionary with a key(prime number result of factor decomposition)
#and a first value of 0. We are going to use this dictionary to store the maximum exponent of a prime factor.
    for x in lista_de_listas:#With this loop we are storing the maximum exponent of the prime factor.
        for i in todos:
            if x.count(i) > my_dictionario_todos[i]:
                my_dictionario_todos[i] = x.count(i)
    mcm = []#In this list we are going to store the result of the prime factor raised to its highest power.
    for key, value in my_dictionario_todos.items():#We use this loop to raise the prime factor to its highest power.
        mcm.append(key ** value)
    print(numpy.prod(mcm))#We compute the product of all the prime factors raised to its highest power.

if __name__ == '__main__':
    my_lista = []#Here we are going to store the numbers whose we are going to find the mcm.
    n = int(input("Introduce la cantidad de números con los que quieres operar: "))#We insert the number of numbers we want to find the mcm.
    for _ in range(n):
        my_lista.append(int(input("Introduce los números de los cuales quieres obtener el mínimo común múltiplo: ")))#We are appending every number to my_lista.
    mcm(my_lista)#We are calling our function.
