from typing import List


def z_function(string: str) -> List[int]:
	""" используется идея z-блоков """
	n = len(string)
	z = [0 for _ in range(n)]
	l, r = 0, 0
	
	for i in range(1, n):
		z[i] = max(0, min(r - i, z[i - l]))
		while i + z[i] < n and string[z[i]] == string[i + z[i]]:
			z[i] += 1
		if i + z[i] > r:
			l = i
			r = i + z[i]
				
	return z
	
	
assert z_function('aaaaa') == [0, 4, 3, 2, 1], f"1. {z_function('aaaaa') }"
assert z_function('aaabaab') == [0, 2, 1, 0, 2, 1, 0], f"2. {z_function('aaabaab')}"
assert z_function('abacaba') == [0, 0, 1, 0, 3, 0, 1], f"3. {z_function('abacaba')}"
assert z_function('aabcaabxaaz') == [0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0], f"3. {z_function('aabcaabxaaz')}"

