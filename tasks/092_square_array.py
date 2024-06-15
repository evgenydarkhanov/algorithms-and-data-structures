def square_array(nums: list[int]) -> list[int]:
	n = len(nums)
	for i in range(n):
		if nums[i] >= 0:
			right = i
			left = i - 1
			break
	
	out = [None for _ in range(n)]
	k = 0
	
	while left > -1 and right < n:
		tmp_l = nums[left]**2
		tmp_r = nums[right]**2
		if tmp_l <= tmp_r:
			out[k] = tmp_l
			left -= 1
		else:
			out[k] = tmp_r
			right += 1
		k += 1
		
	while left > -1:
		out[k] = nums[left]**2
		left -= 1
		k += 1
		
	while right < n:
		out[k] = nums[right]**2
		right += 1
		k += 1
	
	return out
	
	
if __name__ == "__main__":
	nums = [-10, -8, -4, 0, 4, 9]
	assert square_array(nums) == [0, 16, 16, 64, 81, 100], square_array(nums)
	
