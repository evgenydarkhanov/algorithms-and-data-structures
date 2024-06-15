import random


def partition(arr: list, left, right):
	pivot = arr[right]
	i = left - 1
	for j in range(left, right):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[right] = arr[right], arr[i+1]
	return i + 1
	
	
def quicksort(arr: list, left, right):
	if left < right:
		q = partition(arr, left, right)
		quicksort(arr, left, q-1)
		quicksort(arr, q+1, right)
	
	
arr = list(range(10))
quicksort(arr, 0, len(arr)-1)

assert arr == list(range(10)), f'1. {arr}'

