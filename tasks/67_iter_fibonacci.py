import time


def list_fibonacci(n: int) -> int:
	result = [None for _ in range(n + 1)]
	result[0], result[1] = 1, 1
	for i in range(2, n + 1):
		result[i] = result[i-1] + result[i-2]
	
	return result[-1]
	

def iter_fibonacci(n: int) -> int:
	f1, f2 = 0, 1
	while n > 0:
		f1, f2 = f2, f1 + f2
		n -= 1
	return f2 

	
if __name__ == "__main__":
	time_1 = time.time()
	print(f'{iter_fibonacci(10)}, {time.time() - time_1:.10f} seconds')
	assert iter_fibonacci(10) == list_fibonacci(10)
	
	time_2 = time.time()
	print(f'{iter_fibonacci(20)}, {time.time() - time_2:.10f} seconds')
	assert iter_fibonacci(20) == list_fibonacci(20)

	time_3 = time.time()
	print(f'{iter_fibonacci(35)}, {time.time() - time_3:.10f} seconds')
	assert iter_fibonacci(35) == list_fibonacci(35)

