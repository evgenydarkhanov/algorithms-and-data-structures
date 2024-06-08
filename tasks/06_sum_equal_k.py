"""Методом двух указателей:
- можно зафиксировать один и бегать вторым по массиву - $O(n^2)$
- можно прикрутить бинарный поиск - $O(log\;n)$
- можно посчитать сумму и сдвигать левый или правый - $O(n)$"""

from typing import Optional, Tuple


def find_sum_k(arr: list, k: int) -> Optional[Tuple[int]]:
	n = len(arr)
	left = 0
	right = n - 1
	while left <= right:
		summa = arr[left] + arr[right] 
		if summa == k:
			return arr[left], arr[right]
		if summa < k:
			left += 1
		if summa > k:
			right -= 1
	return None
	
	
arr = list(range(10))

assert find_sum_k(arr, 10) == (1, 9), f'1. {find_sum_k(arr, 10)}'
assert find_sum_k(arr, 7) == (0, 7), f'2. {find_sum_k(arr, 7)}'
assert find_sum_k(arr, 12) == (3, 9), f'3. find_sum_k(arr, 12)'
assert find_sum_k(arr, 100) is None, f'4. {find_sum_k(arr,100)}'
