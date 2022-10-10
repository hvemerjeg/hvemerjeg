#THIS CODE IS THE SOLUTION FOR A HACKERRANK PROBLEM CALLED "DIAGONAL_DIFFERENCE"
#The problem is the following:
"""Given a square matrix, calculate the absolute difference between the sums of its diagonals
For example, the following square matrix:
                1 2 3
                4 5 6
                9 8 9
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15-17| = 2"""
def diagonal_difference(matriz):#This our function that will hold the code to find the diagonal difference.
    diagonal_principal = sum([matriz[i][i] for i in range(len(my_matriz))])#We make use of the built-in function called "sum" to get the sum of all the elements that forms
#the principal diagonal. Notice that the main diagonal is formed by the elements in the position of ij where i = j(i represents the rows and j the columns). So we can say that 
#the element in the position ii is the same as ij, where this time the second i represents the columns: my_matriz[i][i]. 
    diagonal_secundaria = sum([matriz[i][(len(matriz) - 1) - i] for i in range(len(my_matriz))])#Once again we make use of the built-in function sum, but this time we are
#getting the sum of the elements that forms the secondary diagonal. In maths we refer to the elements of the secondary diagonal as the elements that holds the position 
#where i + j = matrix dimension + 1, where i is for rows and j is for columns. But since python starts the array indexing at zero, we consider that the
#secondary diagonal is formed by the elements that holds the position ij where i + j = length of the matrix - 1.  
#Because we are iterating through i, we need to see the relationship betwwen i and j for the elements of the secondary diagonal. This relationship is inversely proportional.
#In a 3x3 matrix the elements that forms the secondary diagonal are the following(starting the count at one): (i=1,j=3),(i=2,j=2),(i=3,j=1). So, when i increases by one
#j decreases by one.
    print(abs(diagonal_principal - diagonal_secundaria))#abs is not related in this case with a strong belly, 
#but for obtaining the absolute value of the principal diagonal minus the secondary diagonal.
    
if __name__ == '__main__':
    my_matriz = []
    n = int(input())
    for i in range(n):
        filas_columnas = list(map(int, input().split(" ", n - 1)))#Using map to convert each input to an int. List is to store all the inputs in a sigle list.
#Split is to get different values in the same line, and we are using a delimiter space, and a limit of entries of values to n - 1. So the list has length n.
        my_matriz.append(filas_columnas)#Appending each list to the created list my_matriz, to create a matrix.
    diagonal_difference(my_matriz)#We call our function.
#I think that this problem was a very easy one, but interesting enough to share.
