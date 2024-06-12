# принимает: количество вершин, список из кортежей (рёбра), x, y
# возвращает: кратчайший путь от x до y или None

"""
n, [(1, 2), (2, 3), (1, 4), (3, 5)], x, y
V = {1 .. n}
1 <= x, y <= n

n = 6
1 <--> 2 --> 3 <--> 5
|     ^
|     |
4 <--> 7           6

# x = 1, y = 5 -> 3
# x = 1, y = 6 -> None
"""

from typing import Optional
from collections import defaultdict


def min_dist(n, edges, x, y) -> Optional[int]:
	""" решение через BFS """
	
	# vertex, distance
	queue = deque([x, 0])
	graph = defaultdict[list]
	
	# adding vertices and edges to graph
	for egde in edges:
		graph[edge[0]].append(edge[1])
	
	visited = [False] * (n + 1)
	visited[x] = True
	
	while queue:
		vertex, distance = queue.popleft()
		for neighbors in graph[vertex]:
			if visited[neightbor]:
				continue
			if neighbor == y:
				return 1
				
			visited[neighbor] = True
			queue.append((neighbor, distance + 1))
	return None
	
