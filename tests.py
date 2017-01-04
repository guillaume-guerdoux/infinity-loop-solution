from generate import *
from connect import *
from useful_functions import *
import itertools

#Generating random grid
print("Génération d'une grille aléatoire")
grid = generate_grid(3)
print(grid)
print("\n---------------------\n")

#"Prettyprinting" the grid
print("Représentation de la grille")
prettyprint(grid)
print("\n---------------------\n")

#Converting the grid in a "byte grid"
print("Conversion de la grille en bits")
byte_grid = grid_to_byte(grid)
print(byte_grid)
print("\n---------------------\n")

#Converting the "byte grid" back to a normal grid
print("Conversion inverse")
new_grid = byte_to_grid(byte_grid)
print(new_grid)
print("\n---------------------\n")

#Giving all possible positions for each square
d = get_domain(byte_grid)
print("Liste des états possibles en effectuant une rotation")
print(d)
print("Pour chaque ligne de la grille, cela donne :")
for i in range(len(d)):
    print("Ligne n°" + str(i))
    print(d[i])
print("(On a ainsi par exemple pour la première case les rotations suivantes possibles :)")
print(d[0][0])
print("\n---------------------\n")

