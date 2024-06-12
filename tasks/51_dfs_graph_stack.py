# зададим ненаправленный граф списком смежности	 
		 
def dfs_traverse(graph, start):
	stack = [start]
	visited = []
	
	while stack:
		vertex = stack.pop()
		
		if vertex not in visited:
			visited.append(vertex)
			stack.extend(graph[vertex])
	
	return visited
	
	
if __name__ == "__main__":
	graph = {'a': ['b', 'c'],
			 'b': ['a', 'd', 'e'],'c': ['a', 'f'],
			 'd': ['b'],
			 'e': ['b', 'f'],
			 'f': ['c', 'e']}
			 
	print(dfs_traverse(graph, 'a'))
	print(dfs_traverse(graph, 'e'))

