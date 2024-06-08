from typing import Optional


def binary_search(arr: list, k: int) -> Optional[int]:
	left = 0
	right = len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == k:
			return arr[mid]
		if k > arr[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return None
			
			
arr = list(range(10**6))
k_1 = 10**5
k_2 = 10**7
k_3 = -1

assert binary_search(arr, k_1) == k_1
assert binary_search(arr, k_2) is None
assert binary_search(arr, k_3) is None

