"""
на вход подаётся массив чисел
каждое число - насколько далеко можно прыгнуть из этой ячейки (меньшие значения тоже допустимы)
находимся в нулевой ячейке. можем ли мы с помощью заданных прыжков добраться до последней ячейки?
"""

# [2, 3, 1, 1, 4] --> True
# 2 --> 3 or 2 --> 1
# [2, 3, 1, 1, 0, 4] --> False


def jumps(nums: list) -> bool:
	# если не можем сдвинуться с первой позиции
	if nums[0] == 0:
		return False
	
	# i - дистанция, если идти +1, jump - дистанция если прыгать?
	jump = 0
	for i in range(len(nums)):
	
		# застряли прыжками в нуле
		if i > jump:
			return False
			
		jump = max(jump, i + nums[i])
		
		if jump >= len(nums) - 1:
			return True
	
	return False
	

if __name__ == "__main__":
	assert jumps([2, 3, 1, 1, 4]), jumps([2, 3, 1, 1, 4])
	assert jumps([2, 3, 1, 1, 0]), jumps([2, 3, 1, 1, 0])
	assert not jumps([2, 3, 1, 1, 0, 4]), jumps([2, 3, 1, 1, 0, 4])

