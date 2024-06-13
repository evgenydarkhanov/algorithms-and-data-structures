match = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
		 'C': 100, 'D': 500, 'M': 1000}


def roman_to_arabic(roman: str) -> int:
	n = len(roman)
	arabic = 0
	i = 0

	while i < n:
		value_1 = match[roman[i]]

		if i + 1 < n:
			value_2 = match[roman[i + 1]]

			if value_1 >= value_2:
				arabic += value_1
				i += 1
			else:
				arabic += value_2 - value_1
				i += 2
		else:
			arabic += value_1
			i += 1

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

