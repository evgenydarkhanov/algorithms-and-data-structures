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
		
		
def invert_tree(root):
	if not root:
		return None
	
	root.left, root.right = root.right, root.left
	invert_tree(root.left)
	invert_tree(root.right)

