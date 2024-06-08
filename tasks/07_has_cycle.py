"""запустим два указателя с разными скоростями
если они сойдутся, то зацикливание есть"""

from __future__ import annotations
from typing import Optional


class Node:
	def __init__(self, key: int, next: Optional[Node] = None):
		self.key = key
		self.next = next
		
		
def has_cycle(root) -> bool:
	slow = root
	fast = root
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if fast is slow:
			return True
	return False
	
	
lst1 = Node(1, next=Node(2, next=Node(3)))

n3 = Node(3)
n2 = Node(2, next=n3)
n3.next = n2
lst2 = Node(1, next=n2)

assert not has_cycle(lst1), '1. {has_cycle(lst1)}'
assert has_cycle(lst2), '2. {has_cycle(lst2)}'
