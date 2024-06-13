"""
функция принимает массив целых чисел
вернуть массив чисел, в котором произведение всех кроме данного
"""

def product_array(arr: list) -> list:
	""" в лоб, без оптимизаций """
	n = len(arr)
	prod = 1
	zeros = 0
	out = [0 for _ in range(n)]
	
	for i in range(n):
		if arr[i] == 0:
			zeros += 1
			if zeros > 1:
				return out
			continue
		else:
			prod *= arr[i]
	
	if zeros == 1:
		for i in range(n):
			if arr[i] == 0:
				out[i] = prod
	else:
		for i in range(n):
			out[i] = prod // arr[i]
	
	return out


def product_array_2(arr: list) -> list:
	"""
	произведение всех чисел слева и справа, кроме самого числа
	деление дороже, нет переполнения
	можно переписать в одном цикле
	"""
	n = len(arr)
	out = [0 for _ in range(n)]
	prod = 1
	
	for i in range(n):
		out[i] = prod
		prod *= arr[i]
	
	prod = 1	
	for i in range(n-1, -1, -1):
		out[i] *= prod
		prod *= arr[i]
	
	return out
	
	
if __name__ == "__main__":
	assert product_array([1, 2, 10, 3]) == [60, 30, 6, 20], product_array([1, 2, 10, 3])
	assert product_array([1, 2, 10, 3, 0]) == [0, 0, 0, 0, 60], product_array([1, 2, 10, 3, 0])
	assert product_array([1, 0, 10, 3, 0]) == [0, 0, 0, 0, 0], product_array([1, 0, 10, 3, 0])
	
	assert product_array_2([1, 2, 10, 3]) == [60, 30, 6, 20], product_array_2([1, 2, 10, 3])
	assert product_array_2([1, 2, 10, 3, 0]) == [0, 0, 0, 0, 60], product_array_2([1, 2, 10, 3, 0])
	assert product_array_2([1, 0, 10, 3, 0]) == [0, 0, 0, 0, 0], product_array_2([1, 0, 10, 3, 0])

