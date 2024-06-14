"""
Дана строка s. Строка состоит из английских букв в нижнем регистре. Необходимо из строки удалить все рядом стоящие повторяющиеся буквы.
Например, в строке xyyx мы должны удалить yy, а после и оставшиеся xx итого после должна получиться пустая строка.
Или же в строке fqffqzzsd после удаления остануться только fsd. Первыми удаляться ff, являющимися третьими и четвертыми символами, затем qq и после уже zz.

using stack
"""


def drop_near_dublicates(string: str) -> str:
	if not string:
		return None
	n = len(string)
	if n == 1:
		return string
		
	stack = [string[0]]
	for char in string[1:]:
		old_char = stack.pop()
		if old_char == char:
			continue
		else:
			stack.append(old_char)
			stack.append(char)

	return ''.join(stack)
	
	
if __name__ == "__main__":
	assert drop_near_dublicates('cdffd') == 'c', drop_near_dublicates('cdffd')
	assert drop_near_dublicates('xyyx') == '', drop_near_dublicates('xyyx')
	assert drop_near_dublicates('fqffqzzsd') == 'fsd', drop_near_dublicates('fqffqzzsd')
	assert drop_near_dublicates('ancdd') == 'anc', drop_near_dublicates('ancdd')

