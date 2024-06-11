from __future__ import annotations
from typing import Optional


class Node:
	def __init__(
			self, key: int,
			left: Optional[Node] = None,
			right: Optional[Node] = None
			):
		
		self.key = key
		self.left = left
		self.right = right
		
		
def dfs_in_order(root):
	""" go left, collecting nodes in stack """
	if not root:
		return None
		
	node = root
	stack = []
	result = []
	
	while stack or node:
		while node:
			stack.append(node)
			node = node.left
		
		node = stack.pop()
		result.append(node.key)
		node = node.right
	
	return result


n13 = Node(13)
n14 = Node(14, left=n13)
n10 = Node(10, right=n14)

n4 = Node(4)
n7 = Node(7)
n6 = Node(6, left=n4, right=n7)
n1 = Node(1)
n3 = Node(3, left=n1, right=n6)

root = Node(8, left=n3, right=n10)

assert dfs_in_order(root) == [1, 3, 4, 6, 7, 8, 10, 13, 14], f'1. {dfs_in_order(root)}'

