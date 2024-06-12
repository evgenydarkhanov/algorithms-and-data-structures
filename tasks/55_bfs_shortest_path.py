# зададим ненаправленный граф списком смежности		 
		 
from collections import deque


def bfs_shortest_path(graph, start, end):
	
	# (vertex, [path])
	queue = deque([(start, [start])])
	
	while queue:
		(vertex, path) = queue.popleft()
		for node in graph[vertex]:
			if node not in path:
				if node == end:
					# yield --> all paths
					# return --> first path
					return path + [node]
				else:
					queue.append((node, path + [node]))
	
			else:
				continue
	
	
if __name__ == "__main__":
	graph = {'a': ['b', 'c'],
			 'b': ['a', 'd', 'e'],'c': ['a', 'f'],
			 'd': ['b'],
			 'e': ['b', 'f'],
			 'f': ['c', 'e']}
			 
	print(bfs_shortest_path(graph, 'a', 'c'))
	print(bfs_shortest_path(graph, 'e', 'd'))

