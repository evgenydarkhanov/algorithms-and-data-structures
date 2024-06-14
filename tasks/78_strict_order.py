"""
Дан массив целых чисел nums. Нужно вернуть длину наибольшего подмассива чисел,
который либо строго возрастает либо строго убывает.
Строго означает, что применяется строгое неравенство


можно за один проход по массиву
"""


def strict_order(nums: list) -> int:
	if not nums:
		return 0
	
	n = len(nums)
	if n == 1:
		return 1	
	if n == 2:
		if nums[0] != nums[1]:
			return 2
		return 1
	
	max_length, count_inc, count_dec = 0, 1, 1
	left, right = 0, 1
	
	while right < n:
		if nums[left] < nums[right]:
			count_inc += 1
			max_length = max(max_length, count_inc)
			right += 1
			left += 1
			
		elif nums[left] > nums[right]:
			count_dec += 1
			max_length = max(max_length, count_dec)
			right += 1
			left += 1
			
		else:
			right += 1
			left += 1
			
	return max_length
	
	
if __name__ == "__main__":
	assert strict_order([1, 2, 4, 5]) == 4, strict_order([1, 2, 4, 5])
	assert strict_order([3, 2, 1]) == 3, strict_order([3, 2, 1])
	assert strict_order([1, 2, 2, 1]) == 2, strict_order([1, 2, 2, 1])
	assert strict_order([1]) == 1, strict_order([1])
	assert strict_order([1, 1]) == 1, strict_order([1, 1])
	assert strict_order([1, 2, 3, 4, 4, 4, 5, 4, 3, 2, 1, 0]) == 6, strict_order([1, 2, 3, 4, 4, 4, 5, 4, 3, 2, 1, 0])

