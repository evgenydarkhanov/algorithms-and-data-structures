def shifttable(pattern: str):
	n = len(pattern)
	table = {}
	table[pattern[-1]] = n
	for i in range(n - 1):
		table[pattern[i]] = n - 1 - i
	
	return table


def boyer_moore_horspool(text: str, pattern: str):
	text = text.lower()
	pattern = pattern.lower()
	
	n = len(text)
	m = len(pattern)
	
	entries = []
	table = shifttable(pattern)
	
	if m > n:
		return entries
	
	i = 0
	while i < (n - m + 1):
		j = m - 1
		while j >= 0 and text[i + j] == pattern[j]:
			j -= 1
			if j == 0:
				entries.append(i + j)

		i += table.get(text[i + j], m)
		
	return entries
	
assert boyer_moore_horspool('abcabcabcd', 'cab') == [2, 5], f"1. {boyer_moore_horspool('abcabcabcd', 'cab')}"
assert boyer_moore_horspool('babac', 'aba') == [1], f"2. {boyer_moore_horspool('babac', 'aba')}"
assert boyer_moore_horspool('aaabaaaaabaaaaabaaaaba', 'abaa') == [2, 8, 14], f"3. {boyer_moore_horspool('aaabaaaaabaaaaabaaaaba', 'abaa')}"
assert boyer_moore_horspool('abcdefg', 'h') == [], f"4. {boyer_moore_horspool('abcdefg', 'h')}"

