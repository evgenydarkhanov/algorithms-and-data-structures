def merge_sort_library(books: list) -> list:
	n = len(books)
	if n <= 1:
		return books
		
	left = merge_sort_library(books[:n//2])
	right = merge_sort_library(books[n//2:])
	
	i, j, k = 0, 0, 0
	out = [None for _ in range(n)]
	
	while i < len(left) and j < len(right):
		if left[i][2] < right[j][2]:
			out[k] = left[i]
			i += 1
			k += 1
		elif left[i][2] > right[j][2]:
			out[k] = right[j]
			j += 1
			k += 1
		else:
			if left[i][1] <=  right[j][1]:
				out[k] = left[i]
				i += 1
				k += 1
			elif left[i][1] > right[j][1]:
				out[k] = right[j]
				j += 1
				k += 1
				
	while i < len(left):
		out[k] = left[i]
		i += 1
		k += 1
		
	while j < len(right):
		out[k] = right[j]
		j += 1
		k += 1
	
	for i in range(n):
		books[i] = out[i]
		
	return books
	
	
if __name__ == "__main__":
	n = int(input())
	books = []
	while data := input():
		books.append(data.split())

	books_sorted = merge_sort_library(books)
	for book in books_sorted:
		print(*book)

