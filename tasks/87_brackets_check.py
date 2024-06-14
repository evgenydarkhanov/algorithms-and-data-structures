"""
проверить является ли последовательность скобок валидной
'({[]})' - True
'{[}' - False

решается с использованием стека

"""

match = {'(': ')',
		 '[': ']',
		 '{': '}'}


def brackets_check(brackets: str) -> bool:
	stack = []
	for bracket in brackets:
		# если скобка открывающая, то кладём на стек
		if bracket in match:
			stack.append(bracket)
			
		elif len(stack) == 0 or bracket != match[stack.pop()]:
			return False
	
	return len(stack) == 0
	
	
if __name__ == "__main__":
	assert brackets_check('()'), brackets_check('()')
	assert not brackets_check('(]'), brackets_check('(]')
	assert brackets_check('{{{[()]}}}'), brackets_check('{{{[()]}}}')
	assert not brackets_check('([{{{)'), brackets_check('([{{{)')

