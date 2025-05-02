"""
У вас есть граф, где каждая вершина представляет человека, а ребро между двумя вершинами означает, что эти два человека друзья.
Найдите, существуют ли три человека, которые все взаимно дружат друг с другом (то есть между каждой парой из трех человек существует ребро).

--> найти цикл из трёх вершин --> сделано dfs'ом, но он ищет любые циклы
"""
from collections import defaultdict


def three_friends(edges: list) -> bool:

	# adding vertices and edges to graph
	graph = defaultdict(list)
	for edge in edges:
		graph[edge[0]].append(edge[1])
	
	start = edges[0][0]
	stack = [start]
	
	visited = set()
	
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex])
			
		else:
			return True
	
	return False

	
if __name__ == "__main__":
	assert three_friends([(1, 2), (2, 3), (1, 3)]), three_friends([(1, 2), (2, 3), (1, 3)])
	assert not three_friends([(1, 2), (2, 3), (1, 4)]), three_friends([(1, 2), (2, 3), (1, 4)])
	assert three_friends([(1, 2), (2, 4), (4, 3), (4, 5), (2, 5), (5, 6), (6, 7)]), three_friends([(1, 2), (2, 4), (4, 3), (4, 5), (2, 5), (5, 6), (6, 7)])
	assert three_friends([(1, 2), (2, 4), (4, 3), (4, 5), (2, 8), (8, 5), (5, 6), (6, 7)]), three_friends([(1, 2), (2, 4), (4, 3), (4, 5), (2, 8), (8, 5), (5, 6), (6, 7)])

