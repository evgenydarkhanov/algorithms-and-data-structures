from __future__ import annotations
from typing import Optional
from collections import deque

# 0. is bst
# 1. root is black
# 2. each red node has black parent
# 3. "black height" is constant for all nodes
# 4. leafs are all black
# будем последовательно проверять эти свойства в каждом узле


class RBNode:
	def __init__(
		self, key, value, color='red',
		parent=None,
		left: Optional[RBNode] = None,
		right: Optional[RBNode] = None
		):
		self.key = key
		self.value = value
		self.color = color
		self.parent = parent
		self.left = left
		self.right = right
		

def is_rb_tree(root, min_value=float('-inf'), max_value=float('inf')):
	if not root:
		return False
	if root.color != 'black':
		return False
		
	queue = deque([0, (None, None), root])
	leaf_h = None
	
	while queue:
		h, (left, right), node = queue.popleft()
		
		if node.color == 'red' and node.parent.color != 'black':
			return False
			
		if node.key < left or node.key > right:
			return False
			
		if node.left:
			left_, right_ = left, node.key
			queue.append((h + int(node.color == 'black'), (left_, right_), node.left))
			
		if node.right:
			left_, right_ = node.key, right
			queue.append((h + int(node.color == 'black'), (left_, right_), node.right))
			
		if not node.left and not node.right:
			if leaf_h is None:
				leaf_h = h
			if leaf_h != h:
				return False
	
	return True


if __name__ == "__main__":
	pass
