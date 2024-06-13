def longest_common_substring(str_1: str, str_2: str):
	""" динамически строим таблицу """
	n = len(str_1)
	m = len(str_2)
	
	table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	max_value = (0, 0, 0)
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if str_1[i-1] != str_2[j-1]:
				table[i][j] = 0
			if str_1[i-1] == str_2[j-1]:
				table[i][j] = table[i-1][j-1] + 1
				if table[i][j] > max_value[0]:
					max_value = (table[i][j], i, j)

	return table, max_value
	
	
def restore_substring(str_1, str_2, table, max_value):
	""" по идее, можно идти сразу по диагонали снизу вверх справа налево """
	n = len(str_1)
	m = len(str_2)
	substring = ''
	i, j = max_value[1], max_value[2]
	
	while len(substring) < max_value[0]:
		if str_1[i-1] == str_2[j-1]:
			substring += str_1[i-1]
			i -= 1
			j -= 1
			
	return substring[::-1]


if __name__ == "__main__":
	str_1 = 'BABCABBA'
	str_2 = 'ABACABA'
	table, max_value = longest_common_substring(str_1, str_2)
	for row in table:
		print(row)
	print()
	print(restore_substring(str_1, str_2, table, max_value))

