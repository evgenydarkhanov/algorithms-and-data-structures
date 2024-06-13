"""функция принимает n - число ступенек, на каждом шаге можем либо наступить на следующую либо через одну
сколько разных путей до верха лестницы существует"""
# вариант с очередью не сработал


def ladder(n: int) -> int:
	# no stairs
	if n == 0:
		return 0
	# one stair	
	if n == 1:
		return 1
	# two stairs
	if n == 2:
		return 2
		
	dp = [0 for _ in range(n + 1)]
	dp[1], dp[2] = 1, 2
	for i in range(3, n + 1):
		dp[i] = dp[i-1] + dp[i-2]
		
	return dp[n]
	
	
if __name__ == "__main__":
	print(ladder(1))
	print(ladder(2))
	print(ladder(3))
	print(ladder(4))
	print(ladder(5))

