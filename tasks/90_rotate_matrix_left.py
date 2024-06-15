def rotate_matrix_left(matrix: list) -> list:
	rot_matrix = [list(row) for row in zip(*matrix)][::-1]
	return rot_matrix


if __name__ == "__main__":
	matrix = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
		]
		
	rot_matrix = [
		[3, 6, 9],
		[2, 5, 8],
		[1, 4, 7]
		]
		
	assert rotate_matrix_left(matrix) == rot_matrix, rotate_matrix_left(matrix)

