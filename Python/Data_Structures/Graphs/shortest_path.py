#THIS IS A CODE TO FIND THE SHORTEST PATH BETWEEN TWO NODES IN A GRAPH
def shortestPath(graph, start, end):
	#chack if start equals end
	if start == end:
		return start
	if start not in graph or end not in graph:
		return False
	#Since I may need (depending on the type of graph) to keep track of the visited nodes I will create an empty set for this purpose
	visited = set()
	#I will use a dictionary to store the path of the visited nodes
	paths = {}
	queue = [] #I will implement the traverse through a breadth-first search
	for neighbor in graph[start]:
		if neighbor == end:
			return [end]
		paths[neighbor] = [neighbor]
		queue.append(neighbor)
	while len(queue):
		current = queue.pop(0) #Since I implementing breadth-first search I will need to apply the principle of FIFO
		if current in visited:
			continue
		visited.add(current)
		for neighbor in graph[current]:
			if neighbor in queue or neighbor in visited:
				continue
			if neighbor == end:
				paths[current].append(neighbor)
				return paths[current]
			paths[current].append(neighbor)
			paths[neighbor] = paths[current]
			del paths[current]
			queue.append(neighbor)
	return False

if __name__ == '__main__':
	graph = {
	'A': ['B', 'C', 'H'],
	'B': ['D'],
	'C': ['D'],
	'D': ['E'],
	'E': ['F'],
	'F': ['G', 'H'],
	'G': [],
	'H': ['I'],
	'I': ['F']
	}
	print(shortestPath(graph, 'H', 'G'))

