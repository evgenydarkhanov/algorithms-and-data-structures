def naive_search(text: str, pattern: str) -> bool:
	n = len(text)
	m = len(pattern)
	if m > n:
		return False
	
	for i in range(n):
		count = 0
		for j in range(m):
			if text[i + j] == pattern[j]:
				count += 1
				if count == m:
					return True
			else:
				break
	return False
	
	
assert naive_search('aaabbbaaa', 'abb') is True, f"1. {naive_search('aaabbbaaa', 'abb')}"
assert naive_search('aaabbbaaa', 'cc') is False, f"2. {naive_search('aaabbbaaa', 'cc')}"
assert naive_search('aaabba', 'abbaaaaaa') is False, f"3. {naive_search('aaabba', 'abbaaaaaa')}"
assert naive_search('aabbbaaa', 'aaa') is True, f"4. {naive_search('aabbbaaa', 'aaa')}"

