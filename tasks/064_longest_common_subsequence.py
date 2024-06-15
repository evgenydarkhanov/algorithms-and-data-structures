def longest_common_subsequence(str_1: str, str_2: str):
	""" динамически строим таблицу """
	n = len(str_1)
	m = len(str_2)
	
	table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if str_1[i-1] == str_2[j-1]:
				table[i][j] = table[i-1][j-1] + 1
			elif str_1[i-1] != str_2[j-1]:
				table[i][j] = max(table[i-1][j], table[i][j-1])
					
	return table
	
	
def restore_subsequence(str_1, str_2, table):
	""" идём по таблице снизу вверх справа налево """
	n = len(str_1)
	m = len(str_2)
	subsequence = ''
	i, j = n, m
	while i > 0 and j > 0:
		if str_1[i-1] == str_2[j-1]:
			subsequence += str_1[i-1]
			i -= 1
			j -= 1
		elif table[i-1][j] == table[i][j]:
			i -= 1
		else:
			j -= 1
			
	return subsequence[::-1]


if __name__ == "__main__":
	str_1 = 'BABCABBA'
	str_2 = 'ABACABA'
	table = longest_common_subsequence(str_1, str_2)
	for row in table:
		print(row)
	print()
	print(restore_subsequence(str_1, str_2, table))

