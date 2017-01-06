import itertools
from generate import *

def get_domain_old(byte_grid):
    """Returns a list with all possible byte permutations for each square
    This may be used to get the domain of the optimization problem
    ___DO NOT USE CURRENTLY___"""
    n = len(byte_grid)
    permutations = [list(set(list(itertools.permutations(byte_grid[i][j])))) for i in range(n) for j in range(n)]
    domain = [0]*n
    for i in range(n):
        domain[i] = [0]*n
        for j in range(n):
            a = permutations[i+j*n]
            domain[i][j] = [0]*len(a)
            for k in range(len(a)):
                domain[i][j][k] = a[k]
    return domain


def shift(l):
    """Shift the rank of a list (eg [1,2,3] returns [2,3,1]
    Used to "rotate" by shifting the bits index"""
    return l[1:] + l[:1]


def get_domain(byte_grid):
    """Returns a list with all possible byte permutations for each square
    This may be used to get the domain of the optimization problem"""
    n = len(byte_grid)
    grid = byte_to_grid(byte_grid)
    domain = [0]*n
    for i in range(n):
        domain[i] = [0]*n
        for j in range(n):
            if 0 < grid[i][j] < 15:
                domain[i][j] = [0]*4
                temp = byte_grid[i][j]
                for k in range(4):
                    domain[i][j][k] = temp
                    temp = shift(temp)
            else:
                domain[i][j] = [0]
                domain[i][j][0] = byte_grid[i][j]
    return domain


def get_domain_adapted(domain):
    n = len(domain)
    final = [set() for x in range(n**2)]
    N = range(n)
    for i in N:
        for j in N:
            final[i+j*n] = set(tuple(i) for i in domain[i][j])
    return final


def get_domain_final(byte_grid):
    return get_domain_adapted(get_domain(byte_grid))
