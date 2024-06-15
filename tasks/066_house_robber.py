# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

#         0 1 2 3 4
# nums = [2,7,9,3,1]
# dp =   [2,7,11,11,12]


def house_robber(nums: list[int]) -> int:
	n = len(nums)
	dp = [0 for _ in range(n)]
	dp[0], dp[1] = nums[0], max(nums[0], nums[1])
	
	for i in range(2, n):
		dp[i] = max(nums[i] + dp[i-2], dp[i-1])
	
	return dp[-1]
	
	
if __name__ == "__main__":
	assert house_robber([1, 2, 3, 1]) == 4, f'1. {house_robber([1, 2, 3, 1])}'
	assert house_robber([2, 7, 9, 3, 1]) == 12, f'2. {house_robber([2, 7, 9, 3, 1])}'

