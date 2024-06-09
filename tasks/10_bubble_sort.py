import random


def bubble_sort(arr: list) -> None:
	n = len(arr)
	for i in range(n):
		swap = False
		for j in range(1, n-i):
			if arr[j-1] > arr[j]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
				swap = True
		if not swap:
			break
			
			
arr = list(range(10))
random.shuffle(arr)
bubble_sort(arr)

assert arr == list(range(10)), f'1. {arr}'
