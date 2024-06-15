def rotate_matrix_right(matrix: list) -> list:
	rot_matrix = [list(row) for row in zip(*matrix[::-1])]
	return rot_matrix
	
	
if __name__ == "__main__":
	matrix = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
		]
		
	rot_matrix = [
		[7, 4, 1],
		[8, 5, 2],
		[9, 6, 3]
		]
		
	assert rotate_matrix_right(matrix) == rot_matrix, rotate_matrix_right(matrix)

