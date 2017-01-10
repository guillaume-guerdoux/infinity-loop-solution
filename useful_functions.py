import itertools


def shift(l):
    """Shift the rank of a list (eg [1,2,3] returns [2,3,1]
    Used to "rotate" by shifting the bits index"""
    return l[1:] + l[:1]


def get_domain(byte_grid):
    """Returns a list with all possible byte permutations for each square
    This may be used to get the domain of the optimization problem"""
    n = len(byte_grid)
    domain = [0]*n
    for i in range(n):
        domain[i] = [0]*n
        for j in range(n):
            domain[i][j] = [0]*4
            temp = byte_grid[i][j]
            for k in range(4):
                domain[i][j][k] = temp
                temp = shift(temp)
    return domain


def get_domain_adapted(domain):
    """Formatting the domain previously obtained to enter it in CSP"""
    n = len(domain)
    final = [set() for x in range(n**2)]
    N = range(n)
    for i in N:
        for j in N:
            final[i*n + j] = set(tuple(i) for i in domain[i][j])
    return final


def get_domain_final(byte_grid):
    """Complete function to feed CSP"""
    return get_domain_adapted(get_domain(byte_grid))


def formatting_grid(grid):
    """Formatting grid into a byte_grid to use bytes as variables in CSP
    The tuple composition is (2⁰, 2¹, 2², 2³)
    referring to the side of the square"""
    n = len(grid)
    byte_grid = [0]*n
    for i in range(n):
        byte_grid[i] = [0]*n
        for j in range(n):
            temp = [0] * 4
            b = list(map(int, bin(grid[i][j])[2:]))
            for k in range(len(b)):
                temp[k] = b[k]
            byte_grid[i][j] = tuple(temp)
    return byte_grid


def formatting_solution(sol, n):
    """Formatting the solution obtained after CSP to be able to
       prettyprint it"""
    grid = [0]*n
    for i in range(n):
        grid[i] = [0]*n
        for j in range(n):
            for k in range(4):
                grid[i][j] += sol[i*n+j][k]*(2**k)
    return grid


# -----------------------------------
# OLD FUNCTIONS
# NOT USED IN PROGRAM ANYMORE
# -----------------------------------


def get_domain_old(byte_grid):
    """Returns a list with all possible byte permutations for each square
    This may be used to get the domain of the optimization problem
    ___NOT IN USE ANYMORE___"""
    n = len(byte_grid)
    permutations = [list(set(list(itertools.permutations(byte_grid[i][j]))))
                    for i in range(n) for j in range(n)]
    domain = [0]*n
    for i in range(n):
        domain[i] = [0]*n
        for j in range(n):
            a = permutations[i+j*n]
            domain[i][j] = [0]*len(a)
            for k in range(len(a)):
                domain[i][j][k] = a[k]
    return domain


def grid_to_byte(grid):
    """Converts a grid in its byte equivalent
    for each square"""
    # Array composition : [2⁰, 2¹, 2², 2³]
    n = len(grid)
    byte_grid = [0]*n
    for i in range(n):
        byte_grid[i] = [0]*n
        for j in range(n):
            byte_grid[i][j] = [0] * 4
            b = list(map(int, bin(grid[i][j])[2:]))
            for k in range(len(b)):
                byte_grid[i][j][k] = b[k]
    return byte_grid


def byte_to_grid(byte_grid):
    """Opposite function of grid_to_byte"""
    n = len(byte_grid)
    grid = [0]*n
    for i in range(n):
        grid[i] = [0]*n
        for j in range(n):
            for k in range(4):
                grid[i][j] += byte_grid[i][j][k]*(2**k)
    return grid


def get_byte_tuple(byte_grid):
    n = len(byte_grid)
    byte_tuple = [0]*n
    for i in range(n):
        byte_tuple[i] = [0]*n
        for j in range(n):
            byte_tuple[i][j] = tuple(byte_grid[i][j])
    return byte_tuple


def get_byte_tuple_back(byte_tuple):
    n = len(byte_tuple)
    byte_grid = [0]*n
    for i in range(n):
        byte_grid[i] = [0]*n
        for j in range(n):
            byte_grid[i][j] = list(byte_tuple[i][j])
    return byte_grid
