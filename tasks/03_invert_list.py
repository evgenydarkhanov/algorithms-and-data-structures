def reverse_list_1(arr: list[int]) -> list[int]:
	return arr[::-1]
	
	
def reverse_list_2(arr: list[int]) -> list[int]:
	pass
	
	
arr = list(range(10))
result = list(range(9, -1, -1))

assert reverse_list_1(arr) == result
