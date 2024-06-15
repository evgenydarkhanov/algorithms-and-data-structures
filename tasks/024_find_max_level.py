from __future__ import annotations
from typing import Optional
from collections import deque


class Node:
	def __init__(
			self, key: int,
			left: Optional[Node] = None,
			right: Optional[Node] = None
			):
		
		self.key = key
		self.left = left
		self.right = right
		
		
def bfs_search_max_level(root):
	if not root:
		return None
		
	queue = deque([(root, 0)])
	result = []
	
	while queue:
		node, level = queue.popleft()
		
		if len(result) <= level:
			result.append(node.key)
			
		elif node.key > result[level]:
			result[level] = node.key
			
		if node.left:
			queue.append((node.left, level+1))
			
		if node.right:
			queue.append((node.right, level+1))

	return result
	

n8 = Node(8)
n6 = Node(6, right=n8)
n3 = Node(3)
n1 = Node(1)
n2 = Node(2, left=n1, right=n3)	
root = Node(5, left=n2, right=n6)

assert bfs_search_max_level(root) == [5, 6, 8], f'1. {bfs_search_max_level(root)}'

