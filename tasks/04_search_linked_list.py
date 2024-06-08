# функция принимает односвязный список и k, вернуть Optional[k]

from __future__ import annotations
from typing import Optional


class Node:
	def __init__(self, key: int, next: Optional[Node] = None):
		self.key = key
		self.next = next
		

def search(root, k) -> Optional[int]:
	if not root:
		return None
	if root.key == k:
		return root.key
	node = root
	while node.next:
		node = node.next
		if node.key == k:
			return node.key
	return None
	
	

node_3 = Node(3)
node_2 = Node(2, next=node_3)
node_1 = Node(1, next=node_2)
root = Node(0, next=node_1)

assert search(root, 0) == 0, '0'
assert search(root, 2) == 2, '2'
assert search(root, 3) == 3, '3'
assert search(root, 5) is None, '5'

