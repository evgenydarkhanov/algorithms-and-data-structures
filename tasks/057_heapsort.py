import heapq
import random


def heapsort(arr: list) -> list:
	h = []
	for elem in arr:
		heapq.heappush(h, elem)
	
	return [heapq.heappop(h) for i in range(len(h))] 
	
	
def heapsort_2(arr: list) -> list:
	heapq.heapify(arr)
	return [heapq.heappop(arr) for i in range(len(arr))]
	

arr = list(range(100))
random.shuffle(arr)
assert heapsort(arr) == list(range(100)), f"1. {heapsort(arr)}"
assert heapsort_2(arr) == list(range(100)), f"2. {heapsort_2(arr)}"

