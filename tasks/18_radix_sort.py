import random


def counting_sort_radix_sort(arr: list, digit, BASE) -> list:
	out = [0 for _ in range(len(arr))]
	tmp = [0 for _ in range(BASE)]
	
	for elem in arr:
		index = (elem // digit) % 10
		tmp[index] += 1
		
	for i in range(1, len(tmp)):
		tmp[i] += tmp[i-1]
	
	for elem in arr[::-1]:
		index = (elem // digit) % 10
		out[tmp[index] - 1] = elem
		tmp[index] -= 1
	
	return out


def radix_sort(arr: list) -> list:
	k = max(arr)
	i = 1
	BASE = 10
	
	while i/k < 1:
		arr = counting_sort_radix_sort(arr, i, BASE)
		i *= 10
	
	return arr
	
	
arr = [17, 23, 907, 135, 5, 10, 999, 245, 9]

assert radix_sort(arr) == sorted(arr), f'1. {radix_sort(arr)}'
