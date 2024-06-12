from typing import Optional


def get_suffixes(string: str) -> Optional[list]:
	string += '$'
	return [string[i:] for i in range(len(string))]
	
	
string = 'xabxac'
assert get_suffixes(string) == ['xabxac$', 'abxac$', 'bxac$', 'xac$', 'ac$', 'c$', '$'], f'{get_suffixes(string)}'

