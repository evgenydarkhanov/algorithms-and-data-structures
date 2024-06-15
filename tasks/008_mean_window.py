from typing import Optional


def mean(arr: list) -> float:
	return sum(arr) / len(arr)


def mean_window(arr: list, k: int) -> Optional[list]:
	n = len(arr)
	if n < k:
		return None
	
	left = 0
	right = k
	out = []
	for i in range(n):
		if right + i == n:
			break
		value = mean(arr[left + i : right + i + 1])
		out.append(value)
	return out


arr = list(range(1, 8))

assert mean_window(arr, 9) is None, f'1. {mean_window(arr, 9)}'
assert mean_window(arr, 3) == [2.5, 3.5, 4.5, 5.5], f'2. {mean_window(arr, 3)}'

