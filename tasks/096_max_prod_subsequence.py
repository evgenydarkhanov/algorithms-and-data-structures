"""
O(n*k)?

делить на первый и умножать на последний не стоит - могут быть нули
"""

def max_prod_subsequence(arr: list, k: int) -> int:
	if k == 1:
		return max(arr)
		
	n = len(arr)
	if k > n or k <= 0:
		return 0
	
	max_prod = 1
	for i in range(n - k + 1):
		prod = 1
		for j in range(k):
			prod *= arr[i + j]
		max_prod = max(max_prod, prod)
		
	return max_prod
	
	
if __name__ == "__main__":
	assert max_prod_subsequence([1, 2, 3, 4, 5], 2) == 20, max_prod_subsequence([1, 2, 3, 4, 5], 2)
	assert max_prod_subsequence([2, 4, 2, 7, 1, 6, 12], 3) == 72, max_prod_subsequence([2, 4, 2, 7, 1, 6, 12], 3)

