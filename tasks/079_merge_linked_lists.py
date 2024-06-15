"""
Дан массив k связных списков, каждый связный список отсортирован в порядке возрастания.

Смёрджите все связные списки в один связный список и верните его.

Пример 1:
Ввод: lists = [[1,4,5],[1,3,4],[2,6]]
Вывод: [1,1,2,3,4,4,5,6]

idea 1. merge two with pointers --> add third --> ... --> add next
idea 2. split them on pairs --> merge and merge
"""
from typing import List, Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
		
def merge_two(head1, head2) -> Optional[ListNode]:
	# creating an output head of SLL
	head = ListNode(val=float('inf'))
	head_return = head
	node_1, node_2 = head_1, head_2
	
	while node_1 and node_2:
		if node_1.val < = node_2.val:
			head.next = node_1
			node_1 = node_1.next
		else:
			head.next = node_2
			node_2 = node_2.next
		head = head.next
		
	while node_1:
		head.next = node_1
		node_1 = node_1.next
		head = head.next
		
	while node_2:
		head.next = node_2
		node_2 = node_2.next
		head = head.next
		
	return head_return.next


def merge_all(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
	n = len(lists)
	interval = 1
	head = merge_two(lists[0], lists[1])
	for i in range(2, n):
		tmp = merge_two(head, lists[i])
		head = tmp
		
	return head

