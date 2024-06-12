def less_naive_search(text: str, pattern: str) -> int:
	n = len(text)
	m = len(pattern)
	if m > n:
		return -1
		
	for i in range(n - m + 1):
		for j in range(m):
			if text[i + j] != pattern[j]:
				break
			if j == m - 1:
				return i
	return -1
	
	
assert less_naive_search('aaabbbaaa', 'abb') == 2, f"1. {less_naive_search('aaabbbaaa', 'abb')}"
assert less_naive_search('aaabbbaaa', 'cc') == -1, f"2. {less_naive_search('aaabbbaaa', 'cc')}"
assert less_naive_search('aaabba', 'abbaaaaaa') == -1, f"3. {less_naive_search('aaabba', 'abbaaaaaa')}"
assert less_naive_search('aabbbaaa', 'aaa') == 5, f"4. {less_naive_search('aabbbaaa', 'aaa')}"

