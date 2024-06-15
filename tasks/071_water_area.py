"""
функция. на вход массив чисел, означающих высоту столбов
между столбами наливается вода
найти такие два столба, которые дают наибольшую площадь воды
ширина - количество интервалов между числами
высота - min(left, right)
оставить два столба, которые дают наибольшую площадь воды
"""

# [1, 8, 6, 2, 5, 4, 8, 3, 7] == 49

def water_area(nums: list) -> int:
	""" по сути полный перебор """
	n = len(nums)
	area = 0
	for left in range(n // 2):
		for right in range(n-1, n//2 - 1, -1):
			height = min(nums[left], nums[right])
			width = right - left
			area = max(height * width, area)
	
	return area
	
	
def water_area_2(nums: list) -> int:
	""" сдвигаем указатели умнее """
	n = len(nums)
	left = 0
	right = n - 1
	area = 0
	while left != right:
		height = min(nums[left], nums[right])
		width = right - left
		area = max(height * width, area)
		if nums[left] < nums[right]:
			left += 1
		else:
			right -= 1
		
	return area

	
if __name__ == "__main__":
	assert water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, water_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
	assert water_area_2([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, water_area_2([1, 8, 6, 2, 5, 4, 8, 3, 7])

