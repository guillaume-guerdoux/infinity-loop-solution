from solve_rotation import solve_by_rotation
from solve_sides import solve_sides
from generate import generate_grid
from connect import prettyprint
from useful_functions import formatting_grid
import time
import copy


'''1. Grid Generation'''
n = 4
print("1. Here is the random generated grid with n = ", n)
initial_grid = generate_grid(n)
prettyprint(initial_grid)

'''2. Solve Grid with solve_sides and no arc_consistency'''
print("2. Grid resolution with Solve_sides algorithm (no arc_consistency)")
start_time = time.time()
grid = formatting_grid(list(initial_grid))
solve_sides(grid)
elapsed_time = time.time() - start_time
print("Time to resolve: " + str(elapsed_time) + " seconds \n")

'''3. Solve Grid with solve_rotation and no arc_consistency'''
print("3. Grid resolution with Solve_rotation algorithm (no arc_consistency)")
start_time = time.time()
solution = solve_by_rotation(copy.deepcopy(initial_grid))
elapsed_time = time.time() - start_time
print("Time to resolve: " + str(elapsed_time) + " seconds \n")

'''4. Solve Grid with solve_sides and arc_consistency'''
print("4. Grid resolution with Solve_sides algorithm (with arc_consistency)")
start_time = time.time()
grid = formatting_grid(list(initial_grid))
solve_sides(grid, arc_consistency=True)
elapsed_time = time.time() - start_time
print("Time to resolve: " + str(elapsed_time) + " seconds \n")

'''5. Solve Grid with solve_rotation and arc_consistency'''
print("5. Grid resolution with Solve_rotation algorithm \
(with arc_consistency)")
start_time = time.time()
solution = solve_by_rotation(copy.deepcopy(initial_grid))
elapsed_time = time.time() - start_time
print("Time to resolve: " + str(elapsed_time) + " seconds \n")

'''6. Test performance for each algorithm with or without arc_consistency'''
print("6. Test performance for each algorithm with or \
without arc_consistency \n")
grid_list = []
time_list = []
for i in range(25):
    grid_list.append(generate_grid(i))
# Time with solve_side and no arc_consistency
start_time = time.time()
for grid in grid_list:
    formatted_grid = formatting_grid(list(grid))
    solve_sides(formatted_grid, arc_consistency=False, print_results=False)
elapsed_time_solve_sides_no_arc_consistency = time.time() - start_time
time_list.append(elapsed_time_solve_sides_no_arc_consistency)
print("SOLVE_SIDE / NO ARC_CONSISTENCY: " +
      str(elapsed_time_solve_sides_no_arc_consistency) + " seconds \n")
# Time with solve_side and arc_consistency
start_time = time.time()
for grid in grid_list:
    formatted_grid = formatting_grid(list(grid))
    solve_sides(formatted_grid, arc_consistency=True, print_results=False)
elapsed_time_solve_sides_arc_consistency = time.time() - start_time
time_list.append(elapsed_time_solve_sides_arc_consistency)
print("SOLVE_SIDE / ARC_CONSISTENCY: " +
      str(elapsed_time_solve_sides_arc_consistency) + " seconds \n")
# Time with solve_rotation and no arc_consistency
start_time = time.time()
for grid in grid_list:
    solve_by_rotation(copy.deepcopy(grid), arc_consistency=False,
                      print_results=False)
elapsed_time_solve_rotation_no_arc_consistency = time.time() - start_time
time_list.append(elapsed_time_solve_rotation_no_arc_consistency)
print("SOLVE_ROTATION / NO ARC_CONSISTENCY: " +
      str(elapsed_time_solve_rotation_no_arc_consistency) + " seconds \n")
# Time with solve_rotation and arc_consistency
start_time = time.time()
for grid in grid_list:
    solve_by_rotation(copy.deepcopy(grid), arc_consistency=True,
                      print_results=False)
elapsed_time_solve_rotation_arc_consistency = time.time() - start_time
time_list.append(elapsed_time_solve_rotation_arc_consistency)
print("SOLVE_ROTATION / ARC_CONSISTENCY: " +
      str(elapsed_time_solve_rotation_arc_consistency) + " seconds \n")

# Test the best algorithm
if min(time_list) == elapsed_time_solve_sides_no_arc_consistency:
    print("Solve Sides with no arc_consistency was the best")
elif min(time_list) == elapsed_time_solve_sides_arc_consistency:
    print("Solve Sides with arc_consistency was the best")
elif min(time_list) == elapsed_time_solve_rotation_no_arc_consistency:
    print("Solve Rotation with no arc_consistency was the best")
elif min(time_list) == elapsed_time_solve_rotation_arc_consistency:
    print("Solve Rotation with arc_consistency was the best")
