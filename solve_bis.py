from CentraleSupelec import CSP
from generate import *
from useful_functions import *

def solve_grid(grid):
    """The grid entered in argument must be properly formatted
    As of now, we are solving the problem with 'byte_tuple' grids (cf generate.py)"""
    n = len(grid)
    N = range(n)

    domain = get_domain_final(grid)

    # Reducing domain using unary constraints

    # Top side
    for i in N:
        domain[i] = set(t for t in domain[i] if t[0] == 0)

    # Left side
    for i in range(n**2):
        if i % n == 0:
            domain[i] = set(t for t in domain[i] if t[1] == 0)

    # Right side
    for i in range(n**2):
        if i % n == n-1:
            domain[i] = set(t for t in domain[i] if t[3] == 0)

    # Bottom side
    for i in range(n**2-n,n**2):
        domain[i] = set(t for t in domain[i] if t[2] == 0)

    print(grid)
    print(domain)

    # Now that we have a domain reduced, we can work on binary constraints using a CSP object

    P = CSP(domain)

    #TODO Rajouter les contraintes unaires, j'ai mis ici que les contraintes binaires (et encore, ça plante pour le moment
    for i in N:
        for j in N:
            a = grid[i][j] #Current square
            if j < n-1: #Everything that is not in the bottom line
                c = grid[i][j + 1]  # Square below
                P.addConstraint(a, c, {(x, y) for x in a for y in c if x[2] == y[0]})
                if i < n-1: #Everyting that is not in the bottom line and the rightest column
                    b = grid[i + 1][j] # Square to the right
                    P.addConstraint(a, b, {(x, y) for x in a for y in b if x[3] == y[1]})
            if j == n: #Only the bottom line
                if i < n-1: #Only the bottom line that is not in the bottom-right corner
                    b = grid[i + 1][j]  # Square to the right
                    P.addConstraint(a, b, {(x, y) for x in a for y in b if x[3] == y[1]})

    count = 0
    for sol in P.solve():
        count += 1

    print("Nodes explored : %i " % P.nodes)
    if count == 0:
        print("There is no solution")
    elif count == 1:
        print("The solution is unique")
    else:
        print("The solution is not unique")


solve_grid(grid_to_byte(generate_grid(3)))
