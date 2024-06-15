def rotate_string(text: str, goal: str) -> bool:
	if len(text) != len(goal):
		return False
	
	return text in (goal + goal)
	
	
text, goal = 'abcde', 'deabc'
assert rotate_string(text, goal) is True, f"1. {rotate_string(text, goal)}"
assert rotate_string('abcde', 'cdea') is False, f"2. {rotate_string('abcde', 'cdea')}"
assert rotate_string('abcde', 'aaaaa') is False, f"3. {rotate_string('abcde', 'aaaaa')}"

