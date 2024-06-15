import random


def calc_minrun(n, MIN_MERGE):
	r = 0
	while n >= MIN_MERGE:
		r |= n & 1
		n >>= 1
	return n + r
	

def insertion_sort_timsort(arr: list):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr
	
	
def timsort(arr: list):
	n = len(arr)
	MIN_MERGE = 64
	
	if n < MIN_MERGE:
		return insertion_sort_timsort(arr)
		
	minrun = calc_minrun(n, MIN_MERGE)
		
	for start in range(0, n, minrun):
		end = min(start + minrun, n)
		arr[start:end] = insertion_sort_timsort(arr[start:end])
		
	# остаётся только смерджить отсортированные подмассивы
	
	return arr
	
	
arr = list(range(1000))
random.shuffle(arr)
timsort(arr)

