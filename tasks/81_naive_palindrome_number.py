"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?
"""


def palindrome_number(num: int) -> bool:
	if num < 0 or (num % 10 == 0 and num != 0):
		return False
	
	digit = 1
	BASE = 10
	
	digits = []
	
	while digit/num < 1:
		digits.append((num // digit) % BASE)
		digit *= 10
		
	n = len(digits)
	for i in range(n // 2):
		if digits[i] == digits[n - i - 1]:
			continue
		return False
	
	return True
	

if __name__ == "__main__":
	assert not palindrome_number(1234), palindrome_number(1234)
	assert palindrome_number(121), palindrome_number(121)
	assert not palindrome_number(-121), palindrome_number(-121)
	assert not palindrome_number(10), palindrome_number(10)
	assert palindrome_number(8), palindrome_number(8)
	assert not palindrome_number(1634560932), palindrome_number(1634560932)

