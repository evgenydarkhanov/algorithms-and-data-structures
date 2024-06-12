from typing import List


def z_function(string: str) -> List[int]:
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
	
	
def z_algorithm(text: str, pattern: str, separator='$'):
	n = len(text)
	m = len(pattern)
	entries = []
	if m > n:
		return entries
	
	string = pattern + separator + text
	z = z_function(string)
	for i in range(m + 1, n + m + 1):
		if z[i] == m:
			entries.append(i - m - 1)
	
	return entries
	
	
assert z_algorithm('abcabcabcd', 'cab') == [2, 5], f"1. {z_algorithm('abcabcabcd', 'cab')}"
assert z_algorithm('babac', 'aba') == [1], f"2. {z_algorithm('babac', 'aba')}"
assert z_algorithm('aaabaaaaabaaaaabaaaaba', 'abaa') == [2, 8, 14], f"3. {z_algorithm('aaabaaaaabaaaaabaaaaba', 'abaa')}"
assert z_algorithm('abcdefg', 'h') == [], f"4. {z_algorithm('abcdefg', 'h')}"

