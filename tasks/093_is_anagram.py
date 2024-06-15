def is_anagram(word_1: str, word_2: str) -> bool:
	if len(word_1) != len(word_2):
		return False
		
	hash_table = {}
	
	for char in word_1:
		hash_table[char] = hash_table.get(char, 0) + 1
	
	for char in word_2:
		if char not in hash_table:
			return False
			
		hash_table[char] -= 1
		
		if hash_table[char] == 0:
			del hash_table[char]
	
	return len(hash_table) == 0


if __name__ == "__main__":
	assert is_anagram('anagram', 'nagaram'), is_anagram('anagram', 'nagaram')
	assert not is_anagram('abcd', 'efgh'), is_anagram('abcd', 'efgh')

