from dataclasses import dataclass
from typing import Sequence
import random


@dataclass(order=True)
class Person:
	name: str = ''
	surname: str = ''
	balance: int = 0
	
	
def counting_sort(persons: Sequence[Person], key) -> Sequence[Person]:
	n = len(persons)
	min_key = min(key(p) for p in persons)
	max_key = max(key(p) for p in persons)
	
	offset = abs(min_key)
	 
	tmp = [0 for _ in range(min_key, max_key + 1)]
	out = [None for _ in range(n)]
	
	for p in persons:
		tmp[key(p) + offset] += 1
		
	for i, c in enumerate(tmp[1:], start=1):
		tmp[i] = tmp[i-1] + c
		
	for i in range(n-1, -1, -1):
		idx = key(persons[i]) + offset
		out[tmp[idx] - 1] = persons[i]
		tmp[idx] -= 1
		
	return out
	

persons_random = [Person(balance = random.randint(-50, 50)) for i in range(20)]
persons_sorted_random = counting_sort(persons_random, key=lambda p: p.balance)

assert persons_sorted_random == sorted(persons_random, key=lambda p: p.balance), f'1. {persons_sorted_random}'

