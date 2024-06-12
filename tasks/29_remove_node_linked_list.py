from __future__ import annotations
from typing import Optional


class Node:
	def __init__(self, key, next: Optional[Node] = None):
		self.key = key
		self.next = next
	
	
def remove_node(head: Node, key) -> Optional[Node]:
	if not head:
		return None
	if head.key == key:
		return head.next
		
	root = head
	node = head
	
	while node.next:
		prev = node
		node = node.next
		if node.key == key:
			prev.next = node.next
			return root
			
	return None


n4 = Node(4)
n3 = Node(3, next=n4)
n2 = Node(2, next=n3)
n1 = Node(1, next=n2)
n0 = Node(0, next=n1)

assert remove_node(n0, 10) is None, f'1. {remove_node(n0, 10)}'
assert remove_node(n0, 2) is n0, f'2. {remove_node(n0, 2)}'
assert remove_node(n0, 0) is n1, f'3. {remove_node(n0, 0)}'
assert remove_node(n1, 4) is n1, f'4. {remove_node(n1, 4)}'

