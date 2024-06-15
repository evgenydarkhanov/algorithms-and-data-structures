from typing import Optional

cache = {}


def fibonacci(n: int) -> int:		
	if n in cache:
		return cache[n]
	
	if n == 0:
		result = 0
	elif n == 1:
		result = 1
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
		
	cache[n] = result
	
	return result
	
	
if __name__ == "__main__":
	for i in range(10):
		print(fibonacci(i), end=' ')
	print()

