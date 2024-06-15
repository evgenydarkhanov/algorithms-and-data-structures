import random


def insertion_sort(arr: list) -> None:
	n = len(arr)
	for i in range(1, n):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	
	
arr = list(range(10))
random.shuffle(arr)
insertion_sort(arr)

assert arr == list(range(10)), f'1. {arr}'

