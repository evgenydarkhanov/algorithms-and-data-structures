"""
воспользуемся препроцессингом и построим массив префиксных сумм
"""


def prefix_sum(arr: list) -> list:
	n = len(arr)
	ps = arr[:]
	for i in range(1, n):
		ps[i] += ps[i-1]
	
	return ps
	

def sum_between_i_j(i, j, ps):
	if i == 0:
		return ps[j]
	return ps[j] - ps[i]


if __name__ == "__main__":
	
