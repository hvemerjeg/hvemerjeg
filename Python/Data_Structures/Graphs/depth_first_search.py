#THIS IS AN IMPLEMENTATION OF THE DEPTH-FIRST SEARCH ALGORITHM.
#This algorithm is used for traversing a graph.
#In this case, I will implement it both with recursion and iteration to traverse an acyclic directed graph.

#Iteration
def depthFirstSearch(graph, source):
	#Depth-first search is implemented by the use of a stack. Remember that a stack follows the principle of LIFO(Last In First Out)
	stack = [source]
	visited ={node: False for node in graph}
	while len(stack):
		current = stack.pop()
		print(current, end=", ")
		visited[current] = True
		for neighbor in graph[current]:
			if visited[neighbor]:
				continue
			stack.append(neighbor)	

#Recursion
def depthFirstSearchrecursive(graph, source, visited=[]):	
	if source not in graph:
		return f"\033[1;31;40mSource not in graph!\033[0m"
	print(source, end=", ")
	visited.append(source)
	for neighbor in graph[source]:
		if neighbor in visited:
			continue
		if neighbor not in graph:
			continue
		depthFirstSearchrecursive(graph, neighbor, visited)

if __name__ == '__main__':
	graph = {'A': ['B', 'C'],
	'B': ['D'],
	'C': ['D'], 
	'D': ['E'],
	'E': [] 
	}
	
	depthFirstSearch(graph, 'A')
	print()
	depthFirstSearchrecursive(graph, 'A')	
