from solve_rotation import solve_by_rotation
from solve_first import solve_grid
from generate import generate_grid
from connect import prettyprint
from useful_functions import formatting_grid
import time

'''1. Grid Generation'''
n = 3
print("1. Here is the random generated grid with n = ", n)
initial_grid = generate_grid(n)
prettyprint(initial_grid)

'''2. Solve Grid with solve_first'''
print("2. Grid resolution with Solve_first algorithm")
start_time = time.time()
grid = formatting_grid(initial_grid)
solve_grid(grid)
elapsed_time = time.time() - start_time
print("Time to resolve: " + str(elapsed_time) + " seconds")

'''3. Solve Grid with solve_rotation'''
print("3. Grid resolution with Solve_rotation algorithm")
start_time = time.time()
solution = solve_by_rotation(initial_grid)
elapsed_time = time.time() - start_time
print("Time to resolve: " + str(elapsed_time) + " seconds")
