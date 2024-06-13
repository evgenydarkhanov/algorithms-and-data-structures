import time


cache = {}

def fibonacci(n: int) -> int:
	if n in cache:
		return cache[n]

	if n == 0:
		result = 1
		
	elif n == 1:
		result = 1
		
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
		
	cache[n] = result
	
	return result


if __name__ == "__main__":
	time_1 = time.time()
	print(f'{fibonacci(10)}, {time.time() - time_1:.10f} seconds')
	
	time_2 = time.time()
	print(f'{fibonacci(20)}, {time.time() - time_2:.10f} seconds')

	time_3 = time.time()
	print(f'{fibonacci(35)}, {time.time() - time_3:.10f} seconds')

