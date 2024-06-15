def odd_forward(nums: list) -> list:
	n = len(nums)
	even_index = 0
	for i in range(n):
		if nums[i] % 2 != 0:
			even_index = min(even_index, i)
		elif nums[i] % 2 == 0:
			nums[i], nums[even_index] = nums[even_index], nums[i]
			even_index += 1
			
	return nums
	
	
if __name__ == "__main__":
	assert odd_forward([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 1, 11, 3, 9], odd_forward([3, 2, 4, 1, 11, 8, 9])

# [2, 4, 3, 1, 8, 11, 9]

