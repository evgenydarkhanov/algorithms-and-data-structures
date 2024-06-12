def floyd_warshall(graph):
	""" Floyd-Warshall's algorithm for adjacency matrix """
	n = len(graph)
	distances = [[float('inf') for _ in range(n)] for _ in range(n)]
	
	for i in range(n):
		for j in range(n):
			if i == j:
				distances[i][j] = 0
			elif graph[i][j] != 0:
				distances[i][j] = graph[i][j]
	
	for k in range(n):
		for i in range(n):
			for j in range(n):
				distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
	
	return distances


if __name__ == "__main__":
	matrix_1 = [[0, 5, float('inf'), 10],
				[float('inf'), 0, 3, float('inf')],
				[float('inf'), float('inf'), 0, 1],
				[float('inf'), float('inf'), float('inf'), 0]]
				
	print(floyd_warshall(matrix_1))

