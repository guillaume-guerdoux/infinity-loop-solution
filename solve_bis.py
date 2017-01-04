from CentraleSupelec import CSP
from generate import *
from useful_functions import *

def solve_grid(byte_grid):
    n = len(byte_grid)
    N = range(n)
    #Forming all states possible
    #TODO Vérifier que c'est possible d'utiliser un tel domaine
    P = CSP(get_domain(byte_grid))

    #TODO Rajouter les contraintes unaires, j'ai mis ici que les contraintes binaires (et encore, ça plante pour le moment
    for i in N:
        for j in N:
            a = byte_grid[i][j] #Current square
            if j < n-1: #Everything that is not in the bottom line
                c = byte_grid[i][j + 1]  # Square below
                P.addConstraint(a, c, {(x, y) for x in a for y in c if x[2] == y[0]})
                if i < n-1: #Everyting that is not in the bottom line and the rightest column
                    b = byte_grid[i+1][j] # Square to the right
                    P.addConstraint(a, b, {(x, y) for x in a for y in b if x[3] == y[1]})
            if j == n: #Only the bottom line
                if i < n-1: #Only the bottom line that is not in the bottom-right corner
                    b = byte_grid[i + 1][j]  # Square to the right
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
