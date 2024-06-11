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
		
		
def dfs_search_stack(root, key):
	if not root:
		return None
		
	stack = [root]
	
	while stack:
		node = stack.pop()
		if node.key == key:
			return node.key
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)

	return None
	

n8 = Node(8)
n6 = Node(6, right=n8)
n3 = Node(3)
n1 = Node(1)
n2 = Node(2, left=n1, right=n3)	
root = Node(5, left=n2, right=n6)

assert dfs_search_stack(root, 5) == 5, f'1. {search_key(root, 5)}'
assert dfs_search_stack(root, 8) == 8, f'2. {search_key(root, 8)}'
assert dfs_search_stack(root, 10) is None, f'3. {search_key(root, 10)}'
assert dfs_search_stack(None, 5) is None, f'4. {search_key(None, 5)}'

