def reverse_list_1(arr: list[int]) -> list[int]:
	n = len(arr)
	result = [0 for _ in range(n)]
	for i in range(n):
		result[i] = arr[n - i - 1]
	return result
	
	
def reverse_list_2(arr: list[int]) -> list[int]:
	n = len(arr)
	result = [0 for _ in range(n)]
	for (i, x) in enumerate(arr):
		result[n - i - 1] = x
	return result
	

def reverse_list_3(arr: list[int]) -> list[int]:
	n = len(arr)
	for i in range(n // 2):
		arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
	return arr

	
arr = list(range(10))
result = list(range(9, -1, -1))

assert reverse_list_1(arr) == result, f'1. {reverse_list_1(arr)}'
assert reverse_list_2(arr) == result, f'2. {reverse_list_2(arr)}'
assert reverse_list_3(arr) == result, f'3. {reverse_list_3(arr)}'

