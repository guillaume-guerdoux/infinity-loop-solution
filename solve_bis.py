from CentraleSupelec import CSP
from generate import *
from connect import *
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

    print(domain)

    # Now that we have a domain reduced, we can work on binary constraints using a CSP object

    P = CSP(domain)

    #TODO Rajouter les contraintes unaires, j'ai mis ici que les contraintes binaires (et encore, ça plante pour le moment
    for i in N:
        for j in N:
            a = domain[i+j*n]#Current square
            if j < n-1: #Everything that is not in the bottom line
                c = domain[i+(j+1)*n] # Square below
                P.addConstraint(i+j*n, i+(j+1)*n, {(x, y) for x in a for y in c if x[2] == y[0]})
                if i < n-1: #Everyting that is not in the bottom line and the rightest column
                    b = domain[(i+1)+j*n] # Square to the right
                    P.addConstraint(i+j*n, (i+1)+j*n, {(x, y) for x in a for y in b if x[3] == y[1]})
            if j == n-1 : #Only the bottom line
                if i < n-1: #Only the bottom line that is not in the bottom-right corner
                    b = domain[(i+1)+j*n]  # Square to the right
                    P.addConstraint(i+j*n, (i+1)+j*n, {(x, y) for x in a for y in b if x[3] == y[1]})

    count = 0
    for sol in P.solve():
        count += 1
        if count == 1:
            print("Solved grid:")
            print(sol)
            s = [0]*n
            for i in N:
                s[i] = [0]*n
                for j in N:
                    s[i][j] = sol[i*n+j]
            x = get_byte_tuple_back(s)
            y = byte_to_grid(x)
            prettyprint(y)

    print("Nodes explored : %i " % P.nodes)
    if count == 0:
        print("There is no solution")
    elif count == 1:
        print("The solution is unique")
    else:
        print("The solution is not unique")


initial_grid = generate_grid(10)
prettyprint(initial_grid)
byte_grid = grid_to_byte(initial_grid)
grid = get_byte_tuple(byte_grid)

solve_grid(grid)

