from typing import List


def naive_z_function(string: str) -> List[int]:
	n = len(string)
	z = [0 for _ in range(n)]
	
	for i in range(1, n):
		suffix = string[i:]
		count = 0
		for j in range(n - i):
			if string[j] == suffix[j]:
				count += 1
			else:
				break
		z[i] = count
				
	return z
	
	
assert naive_z_function('aaaaa') == [0, 4, 3, 2, 1], f"1. {naive_z_function('aaaaa') }"
assert naive_z_function('aaabaab') == [0, 2, 1, 0, 2, 1, 0], f"2. {naive_z_function('aaabaab')}"
assert naive_z_function('abacaba') == [0, 0, 1, 0, 3, 0, 1], f"3. {naive_z_function('abacaba')}"
assert naive_z_function('aabcaabxaaz') == [0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0], f"3. {naive_z_function('aabcaabxaaz')}"

