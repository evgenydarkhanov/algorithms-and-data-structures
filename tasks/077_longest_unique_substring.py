"""
Дана строка s, найти длину наибольшей подстроки, содержащую уникальные символы (без повторений).

Пример 1
Ввод: "abcabcbb"
Вывод: 3

Пример 2
Ввод: "pwwhkew"
Вывод: 4

Пример 3
Ввод: "abcdef"
Вывод: 6

sliding window
"""

def longest_unique_substring(string: str) -> int:
	n = len(string)
	
	seen = set()
	
	left = 0
	right = 0
	max_length = 0
	
	while left < n and right < n:
		if string[right] not in seen:
			seen.add(string[right])
			right += 1
			max_length = max(max_length, right - left)
			
		else:
			seen.remove(string[left])
			left += 1
	
	return max_length


if __name__ == "__main__":
	assert longest_unique_substring('abcabcbb') == 3, longest_unique_substring('abcabcbb')
	assert longest_unique_substring('pwwhkew') == 4, longest_unique_substring('pwwhkew')
	assert longest_unique_substring('abcdef') == 6, longest_unique_substring('abcdef')
	assert longest_unique_substring('aaaaaaaaabcdaaaaaa') == 4, longest_unique_substring('aaaaaaaaabcdaaaaaa') 

