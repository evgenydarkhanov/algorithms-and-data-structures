"""
два числа для вершин и третье число для веса ребра, два числа, представляющих начальный и конечный перекрестки


Длительность наиболее краткого пути. Если такого пути нет, то вывести "No path found"

solution by dijkstra
"""
import heapq


def shortest_path_crossroads(edges, points):
	# num of vertices
	m = max(edges, key=lambda x: x[0])[0]
	k = max(edges, key=lambda x: x[1])[1]
	
	n = max(m, k)
	
	start = points[0]
	finish = points[1]
	
	graph = [[0 for _ in range(n)] for _ in range(n)]
	for edge in edges:
		# because of 0 or 1 indexing
		graph[edge[0]][edge[1]] = edge[2]
		graph[edge[1]][edge[0]] = edge[2]
	
	distances = [float('inf') for _ in range(n)]
	distances[start] = 0
	
	# priority queue
	queue = [(0, start)]
	
	while queue:
		dist, vertex = heapq.heappop(queue)
		if dist > distances[vertex]:
			continue
			
		# neighbors of popped vertex
		for neighbor in range(n):
			if graph[vertex][neighbor] > 0:
				distance = dist + graph[vertex][neighbor]
				
				# relaxing??
				if distance < distances[neighbor]:
					distances[neighbor] = distance
					heapq.heappush(queue, (distance, neighbor))
	
	result = "None" if distances[finish] == float('inf') else distances[finish]
	return result


if __name__ == "__main__":
	edges = [(0, 1, 5), (0, 2, 3), (1, 2, 2)]
	points = [0, 2]
	assert shortest_path_crossroads(edges, points) == 3, shortest_path_crossroads(edges, points)

