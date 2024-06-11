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
		
		
def is_bst(root, min_value=float('-inf'), max_value=float('inf')) -> bool:
	if not root:
		return True
	
	if not (min_value <= root.key <= max_value):
		return False

	return (
		is_bst(root.left, min_value, root.key)
		and
		is_bst(root.right, root.key, max_value))


n13 = Node(13)
n14 = Node(14, left=n13)
n10 = Node(10, right=n14)

n4 = Node(4)
n7 = Node(7)
n6 = Node(6, left=n4, right=n7)
n1 = Node(1)
n3 = Node(3, left=n1, right=n6)

root = Node(8, left=n3, right=n10)

assert is_bst(root) is True, f'1. {is_bst(root)}'

