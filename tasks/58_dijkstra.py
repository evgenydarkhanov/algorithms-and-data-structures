import heapq


def dijkstra(graph, start):
	""" Dijkstra's algorithm for adjacency matrix """
	
	# num of vertices
	n = len(graph)
	
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
			
	return distances
	
	
if __name__ == "__main__":
	adjacency_matrix = [[0, 3, 1, 3, 0, 0],
						[3, 0, 4, 0, 0, 0],
						[1, 4, 0, 0, 7, 5],
						[3, 0, 0, 0, 0, 2],
						[0, 0, 7, 0, 0, 4],
						[0, 0, 5, 2, 4, 0]]
						
	print(dijkstra(adjacency_matrix, 0))

