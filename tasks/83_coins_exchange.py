def exchange(coins: list[int], money: int) -> list:
	""" greedy """
	result = []
	i = len(coins) - 1
	while money > 0:
		while i > -1:
			if money >= coins[i]:
				money -= coins[i]
				result.append(coins[i])
				continue
			else:
				i -= 1
				continue
		break
	if money != 0:
		return []
	return result
	
	
if __name__ == "__main__":
	assert exchange([1, 2, 5, 10], 11) == [10, 1]
	assert exchange([1, 2, 5], 11) == [5, 5, 1]
	assert exchange([1, 2, 5, 10], 9) == [5, 2, 2]
	assert exchange([2, 5, 10], 1) == []

