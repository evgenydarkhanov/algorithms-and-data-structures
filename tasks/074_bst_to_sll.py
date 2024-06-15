"""
функция принимает binary-search tree возвращает single-linked list
элементы в порядке возрастания
--> можно обойти элементы в порядке возрастания и добавлять их к списку
dfs нерекурсивный
"""
from __future__ import annotations
from typing import Optional


class TreeNode:
	def __init__(self, key,
				 left: Optional[TreeNode] = None,
				 right: Optional[TreeNode] = None):
				 
		self.key = key
		self.left = left
		self.right = right
				 
				 
class ListNode:
	def __init__(self, key, next: Optional[ListNode] = None):
		self.key = key
		self.next = next
		
		
def bst_to_sll(root: TreeNode) -> Optional[ListNode]:
	if not root:
		return None
	
	stack = []
	node = root
	list_node = None
	result = None
	
	while stack or node:
		while node:
			stack.append(node)
			node = node.left
		
		node = stack.pop()
		
		if not list_node: 
			list_node = ListNode(key=node.key)
			result = list_node
		else:
			list_node.next = ListNode(key=node.key)
			list_node = list_node.next
			
		node = node.right
	
	return result


if __name__ == "__main__":
	pass

