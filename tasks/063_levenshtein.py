# можно не делать отдельную функцию для подсчёта элемента матрицы
# можно не хранить всю матрицу

def levenshtein(str_1: str, str_2: str):
	n, m = len(str_1), len(str_2)
	
	current_row = range(n + 1)
	for i in range(1, m + 1):
		previous_row, current_row = current_row, [i] + [0] * n
		for j in range(1, n + 1):
			add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
			if str_1[j - 1] != str_2[i - 1]:
				change += 1
			
			current_row[j] = min(add, delete, change)
	
	return current_row[n]
	

if __name__ == "__main__":
	str_1 = 'гибралтар'
	str_2 = 'лабрадор'
	print(levenshtein(str_1, str_2))
	
