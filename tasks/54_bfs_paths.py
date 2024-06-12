# зададим ненаправленный граф списком смежности		 

from collections import deque


def bfs_paths(graph, start, end):
	
	# (vertex, [path])
	queue = deque([(start, [start])])
	
	while queue:
		(vertex, path) = queue.popleft()
		for node in graph[vertex]:
			if node not in path:
				if node == end:
					# yield --> all paths
					# return --> first path
					yield path + [node]
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
			 
	print(list(bfs_paths(graph, 'a', 'c')))
	print(list(bfs_paths(graph, 'e', 'd')))

