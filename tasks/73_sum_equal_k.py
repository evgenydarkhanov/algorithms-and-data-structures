"""
функция принимает неотсортированный массив чисел и k
вернуть индексы чисел, сумма которых == k
тип чисел: int

используем словарь для решения за линию
"""
from typing import Optional


def sum_is_equal_to_k(arr: list[int], target: int) -> list:
	if len(arr) < 2:
		return []
		
	visited = {}
	for index, value in enumerate(arr):
		need = target - value
		if need in visited:
			return [visited[need], index]
			
		visited[value] = index
	
	return []
	
	
if __name__ == "__main__":
	assert sum_is_equal_to_k([1, 3, 4, 5, 6], 10) == [2, 4], sum_is_equal_to_k([1, 3, 4, 5, 6], 10) 
	assert sum_is_equal_to_k([1, 3, 4, 5, 6], 100) == [], sum_is_equal_to_k([1, 3, 4, 5, 6], 100)
	assert sum_is_equal_to_k([1, 3, 4, 5, 6], 1) == [], sum_is_equal_to_k([1, 3, 4, 5, 6], 1)
	assert sum_is_equal_to_k([], 1) == [], sum_is_equal_to_k([])
	assert sum_is_equal_to_k([2, 3], 5) == [0, 1], sum_is_equal_to_k([])
	assert sum_is_equal_to_k([2, 3], 6) == [], sum_is_equal_to_k([])

