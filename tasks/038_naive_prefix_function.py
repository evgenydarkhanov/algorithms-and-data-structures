from typing import List


def naive_prefix_function(string: str) -> List[int]:
	n = len(string)
	prefixes = [0 for _ in range(n)]
	for i in range(n):
		for j in range(i):
			# если префикс (срез среза спереди) == суффикс (срез среза сзади)
			if string[:j + 1] == string[i - j:i + 1]:
				# записываем в массив длину среза
				prefixes[i] = j + 1
				
	return prefixes
	
	
assert naive_prefix_function('abcabcd') == [0, 0, 0, 1, 2, 3, 0], f"1. {naive_prefix_function('abcabcd')}"
assert naive_prefix_function('aaaabaaaa') == [0, 1, 2, 3, 0, 1, 2, 3, 4], f"2. {naive_prefix_function('aaaabaaaa')}"
assert naive_prefix_function('abcdef') == [0, 0, 0, 0, 0, 0], f"3. {naive_prefix_function('abcdef')}"

