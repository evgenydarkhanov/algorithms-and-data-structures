import random


def gnome_sort(arr: list) -> None:
	n = len(arr)
	i = 1
	while i < n:
		if arr[i] >= arr[i-1]:
			i += 1
			continue
		else:
			arr[i], arr[i-1] = arr[i-1], arr[i]
			i -= 1
			if i == 0:
				i += 1
	


arr = list(range(10))
random.shuffle(arr)
gnome_sort(arr)

assert arr == list(range(10)), f'1. {arr}'

