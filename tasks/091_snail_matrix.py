def matrix_rotate_left(matrix: list) -> list:
	rot_matrix = [list(row) for row in zip(*matrix)][::-1]
	return rot_matrix


def snail_traverse_matrix(matrix: list) -> list:
	snail = []
	while matrix:
		snail.extend(matrix[0])
		matrix = matrix_rotate_left(matrix[1:])
	return snail


if __name__ == "__main__":
	matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]
		]
		
	snail = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
		
	assert snail_traverse_matrix(matrix) == snail, snail_traverse_matrix(matrix)

