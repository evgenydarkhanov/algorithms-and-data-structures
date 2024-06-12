def naive_rotate_string(text: str, goal: str) -> bool:
	if len(text) != len(goal):
		return False
	
	for i in range(len(text)):
		if text == goal[i:] + goal[:i]:
			return True
	return False
	
	
text, goal = 'abcde', 'deabc'
assert naive_rotate_string(text, goal) is True, f"1. {naive_rotate_string(text, goal)}"
assert naive_rotate_string('abcde', 'cdea') is False, f"2. {naive_rotate_string('abcde', 'cdea')}"
assert naive_rotate_string('abcde', 'aaaaa') is False, f"3. {naive_rotate_string('abcde', 'aaaaa')}"

