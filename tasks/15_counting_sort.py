import random


def counting_sort(arr: list) -> list:
	k = max(arr)
	n = len(arr)
	
	tmp = [0 for _ in range(k + 1)]
	out = [0 for _ in range(n)]
	
	for elem in arr:
		tmp[elem] += 1
		
	for i in range(1, k + 1):
		tmp[i] += tmp[i-1]
		
	for i in range(n-1, -1, -1):
		out[tmp[arr[i]] - 1] = arr[i]
		tmp[arr[i]] -= 1
	
	return out


arr = list(range(10))
random.shuffle(arr)

assert counting_sort(arr) == list(range(10)), f'1. {counting_sort(arr)}'

