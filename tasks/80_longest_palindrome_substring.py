"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

dynamic programming
"""
from typing import Optional


def longest_palindrom_substring(string: str) -> Optional[str]:
	n = len(string)
	
	dp = [[False for _ in range(n)] for _ in range(n)]
	
	# one char is always a palindrome
	for i in range(n):
		dp[i][i] = True
		
	# начало подстроки палиндрома
	start = 0
	max_length = 1
	
	# для всех подстрок длиной от 2
	for l in range(2, n + 1):
		
		# начало и конец подстроки
		for i in range(n - l + 1):
			j = i + l - 1
			# если символы на концах подстроки совпадают и внутри тоже палиндром,
			# то подстрока также является палиндромом
			if string[i] == string[j] and (l == 2 or dp[i+1][j-1]):
				dp[i][j] = True
			if l > max_length:
				start = i
				max_length = l
	
	return string[start : start + max_length]
	
	
if __name__ == "__main__":
	assert longest_palindrom_substring('abccba') == 'abccba', longest_palindrom_substring('abccba')
	assert longest_palindrom_substring('babad') == 'bab' or 'aba', longest_palindrom_substring('babad')
	assert longest_palindrom_substring('cbbd') == 'cbbd', longest_palindrom_substring('cbbd')

