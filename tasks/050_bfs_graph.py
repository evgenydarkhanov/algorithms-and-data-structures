# зададим ненаправленный граф списком смежности

from collections import deque
		 
		 
def bfs_traverse(graph, start):
	queue = deque([start])
	visited = []
	
	while queue:
		vertex = queue.popleft()
		
		if vertex not in visited:
			visited.append(vertex)
			queue.extend(graph[vertex])
	
	return visited
	
	
if __name__ == "__main__":
	graph = {'a': ['b', 'c'],
			 'b': ['a', 'd', 'e'],'c': ['a', 'f'],
			 'd': ['b'],
			 'e': ['b', 'f'],
			 'f': ['c', 'e']}
			 
	print(bfs_traverse(graph, 'a'))
	print(bfs_traverse(graph, 'e'))

