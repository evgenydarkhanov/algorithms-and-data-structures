from typing import List


def less_naive_z_function(string: str) -> List[int]:
	n = len(string)
	z = [0 for _ in range(n)]
	
	for i in range(1, n):
		# пока находимся в пределах строки - переставляем два указателя
		# один в начале строки, другой в начале суффикса
		while i + z[i] < n and string[z[i]] == string[i + z[i]]:
			z[i] += 1
				
	return z
	
	
assert less_naive_z_function('aaaaa') == [0, 4, 3, 2, 1], f"1. {less_naive_z_function('aaaaa') }"
assert less_naive_z_function('aaabaab') == [0, 2, 1, 0, 2, 1, 0], f"2. {less_naive_z_function('aaabaab')}"
assert less_naive_z_function('abacaba') == [0, 0, 1, 0, 3, 0, 1], f"3. {less_naive_z_function('abacaba')}"
assert less_naive_z_function('aabcaabxaaz') == [0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0], f"3. {less_naive_z_function('aabcaabxaaz')}"

