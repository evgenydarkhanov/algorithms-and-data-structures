from typing import Optional


def linear_search(arr: list, k: int) -> Optional[int]:
	for i in range(len(arr)):
		if arr[i] == k:
			return arr[i]
	return None
			
			
arr = list(range(10**6))
k_1 = 10**5
k_2 = 10**7
k_3 = -1

assert linear_search(arr, k_1) == k_1
assert linear_search(arr, k_2) is None
assert linear_search(arr, k_3) is None

