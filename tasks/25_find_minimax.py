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
		
		
def find_min(root):
	if not root:
		return None
	node = root
	
	while node.left:
		node = node.left
		
	return node.key
	
	
def find_max(root):
	if not root:
		return None
	node = root
	
	while node.right:
		node = node.right
		
	return node.key
	

n13 = Node(13)
n14 = Node(14, left=n13)
n10 = Node(10, right=n14)

n4 = Node(4)
n7 = Node(7)
n6 = Node(6, left=n4, right=n7)
n1 = Node(1)
n3 = Node(3, left=n1, right=n6)

root = Node(8, left=n3, right=n10)

assert find_min(root) == 1, f'1. find_min(root) '
assert find_max(root) == 14, f'2. find_max(root) '

