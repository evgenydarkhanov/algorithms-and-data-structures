import random


def merge_sort(arr: list) -> list:
	length = len(arr)
	if length <= 1:
		return arr
		
	left = merge_sort(arr[:length//2])
	right = merge_sort(arr[length//2:])
	
	n, m, k = 0, 0, 0
	out = [None for _ in range(length)]
	
	while n < len(left) and m < len(right):
		if left[n] <= right[m]:
			out[k] = left[n]
			n += 1
		else:
			out[k] = right[m]
			m += 1
		k += 1
		
	while n < len(left):
		out[k] = left[n]
		n += 1
		k += 1

	while m < len(right):
		out[k] = right[m]
		m += 1
		k += 1
	
	for i in range(length):
		arr[i] = out[i]
	
	return arr
	
	
arr = list(range(100))
random.shuffle(arr)
result = merge_sort(arr)

assert result == list(range(100)), f'1. {result}'

