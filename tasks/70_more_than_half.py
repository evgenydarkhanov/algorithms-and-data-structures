"""
функция принимает массив чисел. одно из чисел занимает больше половины массива
найти это число
"""
# [1, 2, 1, 3, 1] --> 1

from typing import Optional


def more_than_half_1(arr: list[int]) -> Optional[int]:
	""" словарём """
	counts = {}
	for i in range(len(arr)):
		if counts.get(arr[i], None):
			counts[arr[i]] += 1
		else:
			counts[arr[i]] = 1
	max_num = max(counts.items(), key=lambda x: x[1])[0]
	return max_num


def more_than_half_2(arr: list[int]) -> Optional[int]:
	""" если это число встречается больше половины раз, то его количество не может быть нивелировано """
	value = None
	count = 0
	
	for num in arr:
		# начинаем заново, если полностью нивелировали
		if count == 0:
			value = num
			
		if num == value:
			count += 1
			
		else:
			count -= 1
			
	return value

	
if __name__ == "__main__":
	assert more_than_half_1([1, 2, 1, 3, 1]) == 1, more_than_half_1([1, 2, 1, 3, 1])
	assert more_than_half_2([1, 2, 1, 3, 1]) == 1, more_than_half_2([1, 2, 1, 3, 1])
	assert more_than_half_1([1, 1, 3]) == 1, more_than_half_1([1, 1, 3])
	assert more_than_half_2([1, 1, 3]) == 1, more_than_half_2([1, 1, 3])

