"""
Дано бинарное дерево поиска в виде массива.
Необходимо найти произведение минимального и максимального значений.
Для этого необходимо вспомнить как бинарное дерево размещается в массиве

root = 0
parent = (i - 1)/2
left = 2i + 1
right = 2i + 2
"""
from typing import Union


def tree_min_max(tree: list) -> Union[int, float]:
	if not tree:
		return -1
	
	n = len(tree)
	if n == 2:
		return tree[0] * tree[1]
	
	left, right = 1, 2
	
	while left < n:
		left = 2 * left + 1
	left = (left - 1) // 2
	
	while right < n:
		right = 2 * right + 2
	right = (right - 1) // 2

		
	return tree[left] * tree[right]
	
	
if __name__ == "__main__":
	assert tree_min_max([16, 11, 18, 9, 13, 17, 21, 7, 10, 12, 15]) == 147, tree_min_max([16, 11, 18, 9, 13, 17, 21, 7, 10, 12, 15])

