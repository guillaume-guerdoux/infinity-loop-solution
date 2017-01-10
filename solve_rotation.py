from CentraleSupelec import CSP
from generate import *
from connect import *


def transform_grid_in_list(grid):
    new_grid = []
    for element in grid:
        for child_element in element:
            new_grid.append(child_element)
    return new_grid


def rotate_grid(grid, rotation, n):
    print("\n---------------------\n")
    print("Solved Grid\n")
    DICT_ROTATION = {(0, 0): 0, (1, 0): 1, (1, 1): 2, (1, 2): 4, (1, 3): 8,
                     (3, 0): 3, (3, 1): 6, (3, 2): 12, (3, 3): 9,
                     (5, 0): 5, (5, 1): 10,
                     (7, 0): 7, (7, 1): 14, (7, 2): 13, (7, 3): 11,
                     (15, 0): 15}
    for i, rotation_number in enumerate(rotation):
        grid[int(i/n)][i % n] = DICT_ROTATION[(grid[int(i/n)][i % n],
                                               rotation_number)]
    return grid


# TODO : for the moment n >= 3 : do it for n=1 or n=2
# TODO : Reduce domain for 5 briques and 0 and 15 : no rotation or just one
def solve_by_rotation(grid):
    # grid = generate_grid(n)
    # grid = [[1, 3, 0, 1], [0, 3, 3, 5], [1, 3, 5, 5], [0, 3, 3, 1]]
    # print("\n---------------------\n")
    # print("Grid to solve\n")
    # prettyprint(grid)
    new_grid = transform_grid_in_list(grid)
    n = len(grid)
    N = range(n**2)
    domain = [set(range(4)) for x in N]

    # REDUCTION DU DOMAINE SELON LE TYPE DE TUILE

    GENERAL_DOMAIN_DICT = {0: {0}, 1: {0, 1, 2, 3}, 3: {0, 1, 2, 3}, 5: {0, 1},
                           7: {0, 1, 2, 3}, 15: {0}}
    for i, tile_number in enumerate(new_grid):
        domain[i] = set(GENERAL_DOMAIN_DICT[tile_number])

    # First : Contrainte unaire : work on N
    TOP_SIDE_CONSTRAINT_DICT = {0: {0}, 1: {1, 2, 3}, 3: {1, 2}, 5: {1},
                                7: {1}}
    LEFT_SIDE_CONSTRAINT_DICT = {0: {0}, 1: {0, 2, 3}, 3: {2, 3}, 5: {0},
                                 7: {2}}
    RIGHT_SIDE_CONSTRAINT_DICT = {0: {0}, 1: {0, 1, 2}, 3: {0, 1}, 5: {0},
                                  7: {0}}
    BOTTOM_SIDE_CONSTRAINT_DICT = {0: {0}, 1: {0, 1, 3}, 3: {0, 3}, 5: {1},
                                   7: {3}}

    # Top side
    for i in range(n):
        if new_grid[i] == 15:
            return grid, "No solution"
        else:
            domain[i] = domain[i] & TOP_SIDE_CONSTRAINT_DICT[new_grid[i]]

    # Left side
    for i in range(n**2):
        if i % n == 0:
            if new_grid[i] == 15:
                return grid, "No solution"
            else:
                domain[i] = domain[i] & LEFT_SIDE_CONSTRAINT_DICT[new_grid[i]]

    # Left side
    for i in range(n**2):
        if i % n == n-1:
            if new_grid[i] == 15:
                return grid, "No solution"
            else:
                domain[i] = domain[i] & RIGHT_SIDE_CONSTRAINT_DICT[new_grid[i]]

    # Bottom side
    for i in range(n**2 - n, n**2):
        if new_grid[i] == 15:
            return grid, "No solution"
        else:
            domain[i] = domain[i] & BOTTOM_SIDE_CONSTRAINT_DICT[new_grid[i]]

    # Create CSP
    solver = CSP(domain)
    # Second : Binary Constraints : use addConstraint
    RIGHT_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT = {0: {}, 1: {3}, 3: {2, 3},
                                                    5: {1}, 7: {1, 2, 3},
                                                    15: {0}}

    LEFT_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT = {0: {}, 1: {1}, 3: {0, 1},
                                                   5: {1}, 7: {0, 1, 3},
                                                   15: {0}}

    RIGHT_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT = {0: {0}, 1: {0, 1, 2},
                                                   3: {0, 1}, 5: {0}, 7: {0},
                                                   15: {}}

    LEFT_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT = {0: {0}, 1: {0, 2, 3},
                                                  3: {2, 3}, 5: {0}, 7: {2},
                                                  15: {}}

    BOTTOM_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT = {0: {}, 1: {2}, 3: {1, 2},
                                                     5: {0}, 7: {0, 1, 2},
                                                     15: {0}}

    TOP_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT = {0: {}, 1: {0}, 3: {0, 3},
                                                  5: {0}, 7: {0, 2, 3},
                                                  15: {0}}

    BOTTOM_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT = {0: {0}, 1: {0, 1, 3},
                                                    3: {0, 3}, 5: {1}, 7: {3},
                                                    15: {}}
    TOP_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT = {0: {0}, 1: {1, 2, 3},
                                                 3: {1, 2}, 5: {1}, 7: {1},
                                                 15: {}}

    for x in range(n**2 - 1):
        # Right side constraint
        if x % n != n-1:
            # Presence of a connecteur
            tile_right_presence_set = \
                RIGHT_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT[new_grid[x]]
            # print(tile_right_presence_set)

            tile_left_presence_set = \
                LEFT_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT[new_grid[x+1]]
            # print(tile_left_presence_set)

            right_side_presence_constraint = \
                {(u, v) for u in tile_right_presence_set
                    for v in tile_left_presence_set}

            # Abscence of a connecteur
            tile_right_abscence_set = \
                RIGHT_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT[new_grid[x]]
            # print(tile_right_abscence_set)

            title_left_abscence_set = \
                LEFT_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT[new_grid[x+1]]
            # print(title_left_abscence_set)

            right_side_absence_constraint = \
                {(u, v) for u in tile_right_abscence_set
                    for v in title_left_abscence_set}
            # print(right_side_absence_constraint)

            right_side_constraint = \
                right_side_presence_constraint | right_side_absence_constraint
            # print(right_side_constraint)
            # if len(right_side_constraint) != 0:
            solver.addConstraint(x, x+1, right_side_constraint)

        # Bottom side constraint
        if x < n**2 - n:
            # Presence of a connecter
            tile_bottom_presence_set = \
                BOTTOM_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT[new_grid[x]]

            tile_top_presence_set = \
                TOP_SIDE_CONNECTOR_PRESENT_CONSTRAINT_DICT[new_grid[x+n]]
            bottom_side_presence_constraint = \
                {(u, v) for u in tile_bottom_presence_set
                    for v in tile_top_presence_set}

            # Absence of a connecter
            tile_bottom_absence_set = \
                BOTTOM_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT[new_grid[x]]
            tile_top_absence_set = \
                TOP_SIDE_CONNECTOR_ABSENT_CONSTRAINT_DICT[new_grid[x+n]]
            bottom_side_absence_constraint = \
                {(u, v) for u in tile_bottom_absence_set
                    for v in tile_top_absence_set}

            bottom_side_constraint = \
                bottom_side_presence_constraint | \
                bottom_side_absence_constraint
            # if len(bottom_side_constraint) != 0:
            solver.addConstraint(x, x+n, bottom_side_constraint)

    # solver.maintain_arc_consistency()
    count = 0
    for sol in solver.solve():
        # print(sol)
        count += 1
        if count == 1:
            new_grid = rotate_grid(grid, sol, n)
            prettyprint(new_grid)

    print("Nodes explored : %i " % solver.nodes)
    if count == 0:
        print("There is no solution.")
    elif count == 1:
        print("The solution is unique.")
    else:
        print("The solution is not unique, there are " +
              str(count) + " solutions.")

if __name__ == "__main__":
    grid = generate_grid(10)
    solution = solve_by_rotation(grid)
