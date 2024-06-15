# зададим ненаправленный граф списком смежности
from typing import Optional


def dfs_traverse(graph, start, visited: Optional[list]=None):

	if visited is None:
		visited = []
		
	visited.append(start)
	
	for vertex in graph[start]:
		if vertex not in visited:
			dfs_traverse(graph, vertex, visited)

	return visited
	
	
if __name__ == "__main__":
	graph = {'a': ['b', 'c'],
			 'b': ['a', 'd', 'e'],'c': ['a', 'f'],
			 'd': ['b'],
			 'e': ['b', 'f'],
			 'f': ['c', 'e']}
			 
	print(dfs_traverse(graph, 'a'))
	print(dfs_traverse(graph, 'e'))

