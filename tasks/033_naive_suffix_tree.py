class SuffixTree:
	def __init__(self, string: str):
		self.string = string + '$'
		self.root = {}
		
	def get_suffixes(self):
		return [self.string[i:] for i in range(len(self.string))]
		
	def _insert_suffix(self, suffix, current_node):
		if suffix[0] not in current_node:
			current_node[suffix[0]] = {}
			
		if len(suffix) > 1:
			self._insert_suffix(suffix[1:], current_node[suffix[0]])
		
	def construct_tree(self):
		suffixes = self.get_suffixes()
		for suffix in suffixes:
			self._insert_suffix(suffix, self.root)
			
		return self.root
		

if __name__ == "__main__":	
	string = 'xabxac'
	sftree = SuffixTree(string)
	print(sftree.get_suffixes())
	for pair in sftree.construct_tree().items():
		print(pair)

