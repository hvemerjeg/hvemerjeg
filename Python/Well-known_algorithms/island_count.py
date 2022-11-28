#THIS CODE IS A SOLUTION OF A WELL-KNOWN CODING PROBLEM CALLED "ISLAND COUNT"
#The task of this problem is, given a matrix where each 1 represents land and each 0 represents water, to return the number of islands. 
#All adjecent ones, either horizontally and vertically are count as a single land. For example:
#	1 0 0
#	1 1 0
#	0 0 1
#We have two lands here: one of length three and one of length one, so we should return two.
#One of the keys to solve this problem is to think of the matrix as a graph and treat it elements as nodes!
#We are going to split this problem in three different functions: 
#One to return the final result and iterate through the elements in the matrix
#Another to traverse through the neighbor nodes of the elements in the matrix
#The last one to find the neighbor nodes of an element
#Let's code
def islandSizes(matrix): #This is the first function.
	result = 0 #Since we need to store the number of islands we are going to create a variable to zero and increment it if needed
	visited = [[False for col in row] for row in matrix] #It is fundamental to keep track of the visited nodes, otherwise we will be lost visiting the same node infinitely. For this 
#purpose we are going to create the same matrix full of False values instead oof 1's and 0's. In case that we visit a element at index i, j we will set the element in this position to True.
	for i in range(len(matrix)): #We iterate through the matrix
		for j in range(len(matrix[i])):
			if visited[i][j]: #If the element is already visited we skip to the next iteration
				continue
			result += traverseNode(i, j, matrix, visited) #Otherwise we enter the function traverseNode
	return result

def traverseNode(i, j, matrix, visited):
	#Breadth-first search is the traverse algorithm that I will implement. You can use a depth-first search too. As you may know the only difference is that the
#breadth-first search uses a queue and the depth-first search uses a stack. Also, we can not implement a breadth-frst search with recursion
	at_least_river = False #I Will use this flag to know if in any moment I hit land
	queue = [[i, j]] #The elements inside the queue are lists containing the indexes i for row and j for columns
	while len(queue): #While the length of the queue is different than 0 we keep the while loop
		current = queue.pop(0) #We take pop an element of the queue. Now current contains a list with indexes i and j
		i = current[0] #Set the first value of this list to i
		j = current[1] #Set the second value of this list to j
		if visited[i][j]: #If we visited this element we continue the while loop
			continue
		visited[i][j] = True #Otherwise we set the element to true in the visited matrix
		if matrix[i][j] == 0: #If the element is 0 we hit river, so we continue to the next iteration
			continue
		at_least_river = True #We hit land
		neighbors = getNeighbors(i, j, matrix, visited) #Getting the neighbors of the element
		for neighbor in neighbors:
			queue.append(neighbor) #Appending the neighbors of the elements to the queue to be visited
	if at_least_river:
		return 1	
	return 0

def getNeighbors(i, j, matrix, visited):
	neighbors = []
	if i > 0 and not visited[i - 1][j]: #If i is bigger than 0 that means that we have an element in the previous row. If that element is not already visited, we are going to append it to
#the neighbors list
		neighbors.append([i - 1, j])
	if i < len(matrix) - 1 and not visited[i + 1][j]:#If i is less than the len of matrix, that means that we have a next row. If that element is not already visited, we are going to append it
#to neighbors too
		neighbors.append([i + 1, j])
	#The same logic is applied to the columns
	if j > 0 and not visited[i][j - 1]:
		neighbors.append([i, j - 1])
	if j < len(matrix[i]) - 1 and not visited[i][j + 1]:
		neighbors.append([i, j + 1])
	return neighbors #We return the neighbors


if __name__ == '__main__':
	#TEST
	matrix = [
	[1, 1, 0],
	[0, 0, 1],
	[1, 0, 0]
	]
	print(islandSizes(matrix))#It should return three.
