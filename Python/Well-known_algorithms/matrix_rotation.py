#Matrix layer rotation
#The task of this problem is to rotate a matrix n times
#For example the following matrix
#	1 2
#	3 4
#After one rotation
#	2 4
#	1 3
#Another example with two rotations:
#Start         First           Second
#     1 2 3 4       2  3  4  5      3  4  5  6
#    12 1 2 5  ->   1  2  3  6 ->   2  3  4  7
#    11 4 3 6      12  1  4  7      1  2  1  8
#    10 9 8 7      11 10  9  8     12 11 10  9
#Notice that all the layers rotates in case that the matrix has more than one layer
#To know more about the problem: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
def matrixRotation(matrix: list, rotations: int):
	matrix_copy = [[column for column in row] for row in matrix] #I will make use of a copy of the matrix so I can map the rotation with this copy an then updated this matrix_copy
#for further rotations
	i = 0 #We are going to start travesing the elements of the matrix at position [0][0]. That is the reason why both i and j equal zero
	j = 0
	#h and t are used to control the number of steps that we need to make in the different directions, because in some cases we will have more than a layer in our matrix.
	#For example in the second matrix given as an example if we are in the outside layer starting at position i = 0 and j = 0 we need to make the element at the current position to be equal to the element at i = 0 j + 1 and move to the next element at i = 0 j + 1 until j is minor than len(matrix[i]) - 1. But if we start at the second layer of the matrix, position i = 1 and j = 1 we need to make the same steps but the limit is not len(matrix[i]) -1 instead len(matrix[i]) - 2. The same logic is applied for t. 
	h = 1
	t = 0
	while rotations > 0: #We are going to apply the logic of the rotations n times where n equals the variable rotations
		rotations -= 1
		x = int(len(matrix) / 2)
		y = int(len(matrix[0]) / 2)
		n_iter = min(x, y) #This logic is for knowing how many layers does the matrix have. For example, if I have a matrix of dimension 4x4 I know that I have two layers to rotate.
#If I have a matrix of dimensions 3x4 I only have one layer to rotate! So we need to divide by two both the length of the row and the length of the column, take the integer part and the minor value between the two divisions.
		for iteration in range(n_iter):
		#We have four directions in our traversal through the matrix.
		#We start at index i = 0 and j = 0. We make this element equal to the element at postion i = 0 and j + 1 and augment j in one. So now we are at position i = 0 and j = 1. This is repeated until j == len(matrix[i]) - h. After that we need to make the current element equal to the element at posiition i + 1 and j = len(matrix[i]) - h. The same logic is repeated in the four directions
			while j < len(matrix[i]) - h:
				matrix[i][j] = matrix_copy[i][j + 1]
				j += 1
			while i < len(matrix) - h:
				matrix[i][j] = matrix_copy[i + 1][j]
				i += 1
			while j > t:
				matrix[i][j] = matrix_copy[i][j - 1]
				j -= 1
			while i > t:
				matrix[i][j] = matrix_copy[i - 1][j]
				i -= 1
			#In case that we have more than one layer we need to augment i and j in one. Also the limits h and t in one.
			i += 1
			j += 1
			h += 1
			t += 1
		i = 0
		j = 0
		h = 1
		t = 0	
		matrix_copy = [[column for column in row] for row in matrix] #After the rotation we update the matrix_copy to be the same as the matrix
	for row in matrix:
		print(*row) #We print the matrix once we completed all the rotations

if __name__ == '__main__':
	#TEST
	matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]
	]
	matrixRotation(matrix, 1)
