def d(str_1, str_2, i, j):
	if i > 0 and j > 0:
		m = 1
		if str_1[i] == str_2[j]:
			m = 0
			
		return min(
					d(str_1, str_2, i, j-1) + 1,
					d(str_1, str_2, i-1, j) + 1,
					d(str_1, str_2, i-1, j-1) + m
			)
		
	elif i == 0 and j == 0:
		return 0
		
	elif i == 0 and j != 0:
		return j
		
	elif i != 0 and j == 0:
		return i
	

def levenshtein(str_1: str, str_2: str) -> int:

	str_1 = ' ' + str_1
	str_2 = ' ' + str_2
	
	n = len(str_1)
	m = len(str_2)
	
	table = [[None for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			table[i][j] = d(str_1, str_2, i, j)
			
	return table
	
	
if __name__ == "__main__":
	str_1 = 'гибралтар'
	str_2 = 'лабрадор'
	print(levenshtein(str_1, str_2)[-1][-1])

