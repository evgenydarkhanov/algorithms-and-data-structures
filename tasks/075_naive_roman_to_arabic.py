"""
Дано число, записанное римскими цифрами,
нужно его конвертировать в обычное с арабскими цифрами.
“XX” -> 20.

решение не учитывает двойное вычитание и ограничение на размеры чисел
"""

def roman_to_arabic(roman: str) -> int:
	if not roman:
		return None
	
	n = len(roman)
	convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	arabic = 0
	to_add = 1
	for i in range(n-1, -1, -1):
		if convert[roman[i]] >= to_add:
			arabic += convert[roman[i]]
		else:
			arabic -= convert[roman[i]]
		to_add = convert[roman[i]]
	
	return arabic


if __name__ == "__main__":
	assert roman_to_arabic('XX') == 20, roman_to_arabic('XX')
	assert roman_to_arabic('XXI') == 21, roman_to_arabic('XXI')
	assert roman_to_arabic('IX') == 9, roman_to_arabic('IX')
	assert roman_to_arabic('XI') == 11, roman_to_arabic('XI')
	
	assert roman_to_arabic('XVII') == 17, roman_to_arabic('XVII')
	assert roman_to_arabic('XXIX') == 29, roman_to_arabic('XXIX')
	assert roman_to_arabic('XLIX') == 49, roman_to_arabic('XLIX')
	assert roman_to_arabic('IV') == 4, roman_to_arabic('IV')
	
	assert roman_to_arabic('MMDCLXXVI') == 2676, roman_to_arabic('MMDCLXXVI')
	assert roman_to_arabic('MCCCLIX') == 1359, roman_to_arabic('MCCCLIX')

