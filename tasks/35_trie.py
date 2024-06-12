from __future__ import annotations
from typing import Optional, Tuple


ALPHABETH_SIZE = 26


class TrieNode:
	def __init__(
		self, label,
		children=[None for _ in range(ALPHABETH_SIZE)],
		is_terminal=False):
		
		self.label = label
		self.children = children
		self.is_terminal = is_terminal


class Trie:
	def __init__(self):
		self.root = TrieNode(label='')
		
	def search(self, search_key) -> Tuple[bool, str]:
		if not search_key:
			return None
			
		search_key = search_key.lower()
		node = self.root
		word = node.label
		
		for char in search_key:
			index = ord(char) - ord('a')
			if node.children[index] is None:
				return (False, word)
			node = node.children[index]
			word += node.label
		
		if not node.is_terminal:
			return (False, word)
		return (True, word)
		
	def insert(self, insert_key):
		if not insert_key:
			return None
			
		insert_key = insert_key.lower()
		
		if self.search_key(insert_key)[0]:
			raise KeyError('exists')
			
		else:
			node = self.root:
			for char in insert_key:
				index = ord(char) - ord('a')
				if node.children[index] is None:
					node.children[index] = TrieNode(label=char)
				node = node.children[index]
			node.is_terminal = True

	def has_prefix(self, prefix):
		if not prefix:
			return None
		prefix = prefix.lower()
		for char in prefix:
			index = ord(char) - ord('a')
			if node.children[index] is None:
				return False
			node = node.children[index]
		return True

