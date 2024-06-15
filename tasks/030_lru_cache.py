class LRUCache:
	def __init__(self, limit):
		self.limit = limit
		self.cache = {}
		
	def __getitem__(self, key):
		if key not in self.cache:
			return None
		value = self.cache[key]
		del self.cache[key]
		self.cache[key] = value
		return value
		
	def __setitem__(self, key, value):
		if key not in self.cache:
			self.cache[key] = value
		else:
			if len(self.cache) == self.limit:
				del self.cache[next(iter(self.cache))]
			self.cache[key] = value

