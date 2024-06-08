# развернуть односвязный список

from __future__ import annotations
from typing import Optional


class Node:
	def __init__(self, key: int, next: Optional[Node] = None):
		self.key = key
		self.next = next
		
		
def reverse_list(root):
	if not root:
		return None
	node = root
	prev = None
	while node:
		next_node = node.next
		node.next = prev
		prev = node
		node = next_node
	return prev


node_3 = Node(3)
node_2 = Node(2, next=node_3)
node_1 = Node(1, next=node_2)
root = Node(0, next=node_1)

result = reverse_list(root)

assert result.key == 3

