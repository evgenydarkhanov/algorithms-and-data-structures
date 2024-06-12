# зададим ненаправленный граф списком смежности		 
		 
def dfs_paths(graph, start, end):
	
	# (vertex, [path])
	stack = [(start, [start])]
	
	while stack:
		(vertex, path) = stack.pop()
		for node in graph[vertex]:
			if node not in path:
				if node == end:
					# yield --> all paths
					# return --> first path
					yield path + [node]
				else:
					stack.append((node, path + [node]))
	
			else:
				continue
	
	
if __name__ == "__main__":
	graph = {'a': ['b', 'c'],
			 'b': ['a', 'd', 'e'],'c': ['a', 'f'],
			 'd': ['b'],
			 'e': ['b', 'f'],
			 'f': ['c', 'e']}
			 
	print(list(dfs_paths(graph, 'a', 'c')))
	print(list(dfs_paths(graph, 'e', 'd')))

