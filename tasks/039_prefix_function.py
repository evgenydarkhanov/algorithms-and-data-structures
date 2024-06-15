from typing import List


def prefix_function(string: str) -> List[int]:
	n = len(string)
	prefixes = [0 for _ in range(n)]
	
	for i in range(1, n):
		k = prefixes[i - 1]
		while k > 0 and string[i] != string[k]:
			k = prefixes[k - 1]
		if string[i] == string[k]:
			k += 1
		prefixes[i] = k
	
	return prefixes
	
	
assert prefix_function('abcabcd') == [0, 0, 0, 1, 2, 3, 0], f"1. {prefix_function('abcabcd')}"
assert prefix_function('aaaabaaaa') == [0, 1, 2, 3, 0, 1, 2, 3, 4], f"2. {prefix_function('aaaabaaaa')}"
assert prefix_function('abcdef') == [0, 0, 0, 0, 0, 0], f"3. {prefix_function('abcdef')}"

