from typing import Optional
import heapq

# [1, 2, 3, 4, 5, 6, 7, 8], 3 --> 6
# [1, 2, 3, 4, 5, 6, 7, 8], 1 --> 8
# [1, 2, 3, 4, 5, 6, 7, 8], 8 --> 1

# будем создавать кучу и добавлять в неё

class NLarge:
	def __init__(self, n):
		self.n = n
		self.h = []
	
	def add(self, elem) -> Optional[int]:
		heapq.heappush(self.h, elem)
		
		if len(self.h) >= self.n:
			while len(self.h) > self.n:
				heapq.heappop(self.h)
			return self.h[0]
		return None
	

nl = NLarge(3)

assert nl.add(1) is None, f'1'
assert nl.add(2) is None, f'2'
assert nl.add(3) == 1, f'3'
assert nl.add(4) == 2, f'4'
assert nl.add(10) == 3, f'6'

