from CentraleSupelec import CSP 
from generate import *

# TODO : for the moment n >= 3 : do it for n=1 or n=2
n=3
grid = generate_grid(n)
'''print(grid)
print("\n---------------------\n")'''

byte_grid = grid_to_byte(grid)
print(byte_grid)

N = range(n*n*4)
#print([set(range(2)) for x in N])
#print(len([set(range(2)) for x in N]))

# First : Contrainte unaire : work on N (addConstraint is only for Binary constraint)
domain = [set([0,1]) for x in N]
print("Domaine de base de longueur " + str(len(domain)))
print(domain)
print("\n---------------------\n")
# Contrainte sur les côtés : réduction du domaine

# Coté du haut
for x in range(3):
	domain[x*4] = set([0])
# Coté de gauche et de droite
for x in range(n**2):
	if x%n == 0:
		domain[x*4 + 1] = set([0])
	if x%n == n-1:
		domain[x*4 + 3] = set([0])
# Coté du bas 
for x in range(n**2 - n, n**2):
	domain[x*4 + 2] = set([0])
print("Domaine réduit par les contraintes extérieures")
print(domain)
