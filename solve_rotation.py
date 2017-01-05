from CentraleSupelec import CSP
from generate import *

def transform_grid_in_list(grid):
	new_grid = []
	for element in grid:
		for child_element in element:
			new_grid.append(child_element)
	return new_grid


# TODO : for the moment n >= 3 : do it for n=1 or n=2

def solve_by_rotation(n):
	grid = generate_grid(n)
	print(grid)
	new_grid = transform_grid_in_list(grid)
	print(new_grid)
	N = range(n**2)
	domain = [set(range(4)) for x in N]
	print(domain)

	TOP_SIDE_CONSTRAINT_DICT = {0: set(range(4)), 1: {1,2,3}, 3: {1,2}, 5: {1,3}, 7: {1}}
	LEFT_SIDE_CONSTRAINT_DICT = {0: set(range(4)), 1: {0,2,3}, 3: {2,3}, 5: {0,2}, 7: {2}}
	RIGHT_SIDE_CONSTRAINT_DICT = {0: set(range(4)), 1: {0,1,2}, 3: {0,1}, 5: {0,2}, 7: {0}}
	BOTTOM_SIDE_CONSTRAINT_DICT = {0: set(range(4)), 1: {0,1,3}, 3: {0,3}, 5: {1,3}, 7: {3}}
	# First : Contrainte unaire : work on N (addConstraint is only for Binary constraint)
	# Top side
	for i in range(n):
		if new_grid[i] == 15:
			return "No solution"
		else:
			domain[i] = domain[i] & TOP_SIDE_CONSTRAINT_DICT[new_grid[i]]

	# Left side
	for i in range(n**2):
		if i%n == 0:
			if new_grid[i] == 15:
				return "No solution"
			else:
				domain[i] = domain[i] & LEFT_SIDE_CONSTRAINT_DICT[new_grid[i]]

	# Left side
	for i in range(n**2):
		if i%n == n-1:
			if new_grid[i] == 15:
				return "No solution"
			else:
				domain[i] = domain[i] & RIGHT_SIDE_CONSTRAINT_DICT[new_grid[i]]

	# Bottom side
	for i in range(n**2 - n, n**2):
		if new_grid[i] == 15:
			return "No solution"
		else:
			domain[i] = domain[i] & BOTTOM_SIDE_CONSTRAINT_DICT[new_grid[i]]
	print(domain)

if __name__ == "__main__":
    print(solve_by_rotation(3))