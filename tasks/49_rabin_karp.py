def rabin_karp(text: str, pattern: str):
	n = len(text)
	m = len(pattern)
	
	entries = []
	if m > n:
		return entries
		
	hP = sum([ord(pattern[i]) for i in range(m)])
	hT = sum([ord(text[i]) for i in range(m)])
	
	for i in range(n - m + 1):
		if hP == hT:
			count = 0
			for j in range(m):
				if pattern[j] == text[i + j]:
					count += 1
					if count == m:
						entries.append(i)
		else:
			if i != n - m:
				hT += ord(text[i + m]) - ord(text[i])
				
	return entries
	
	
assert rabin_karp('abcabcabcd', 'cab') == [2, 5], f"1. {rabin_karp('abcabcabcd', 'cab')}"
assert rabin_karp('babac', 'aba') == [1], f"2. {rabin_karp('babac', 'aba')}"
assert rabin_karp('aaabaaaaabaaaaabaaaaba', 'abaa') == [2, 8, 14], f"3. {rabin_karp('aaabaaaaabaaaaabaaaaba', 'abaa')}"
assert rabin_karp('abcdefg', 'h') == [], f"4. {rabin_karp('abcdefg', 'h')}"

