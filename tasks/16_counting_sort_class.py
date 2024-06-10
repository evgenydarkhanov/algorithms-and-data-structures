from dataclasses import dataclass
from typing import Sequence
import random


@dataclass(order=True)
class Person:
	name: str = ''
	surname: str = ''
	age: int = 0
	address: str = ''
	
	
def counting_sort(persons: Sequence[Person], key) -> Sequence[Person]:
	n = len(persons)
	max_key = max(key(p) for p in persons)
	
	tmp = [0 for _ in range(max_key + 1)]
	out = [None for _ in range(n)]
	
	for p in persons:
		tmp[key(p)] += 1
		
	for i, c in enumerate(tmp[1:], start=1):
		tmp[i] = tmp[i-1] + c
		
	for i in range(n-1, -1, -1):
		idx = key(persons[i])
		out[tmp[idx] - 1] = persons[i]
		tmp[idx] -= 1
		
	return out
	

persons_random = [Person(age = random.randint(10, 50)) for i in range(10)]
persons_sorted_random = counting_sort(persons_random, key=lambda p: p.age)

assert persons_sorted_random == sorted(persons_random, key=lambda p: p.age), f'1. {persons_sorted_random}'

