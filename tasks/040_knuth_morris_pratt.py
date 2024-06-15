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
	
	
def knuth_morris_prath(text: str, pattern: str, separator = '$'):
	n = len(text)
	m = len(pattern)
	
	entries = []
	if m > n:
		return entries
	
	string = pattern + separator + text
	prefixes = prefix_function(string)
	
	for i in range(m + 1, n + m + 1):
		if prefixes[i] == m:
			entries.append(i - 2*m)
	
	return entries
	
	
assert knuth_morris_prath('abcabcabcd', 'cab') == [2, 5], f"1. {knuth_morris_prath('abcabcabcd', 'cab')}"
assert knuth_morris_prath('babac', 'aba') == [1], f"2. {knuth_morris_prath('babac', 'aba')}"
assert knuth_morris_prath('aaabaaaaabaaaaabaaaaba', 'abaa') == [2, 8, 14], f"3. {knuth_morris_prath('aaabaaaaabaaaaabaaaaba', 'abaa')}"
assert knuth_morris_prath('abcdefg', 'h') == [], f"4. {knuth_morris_prath('abcdefg', 'h')}"

