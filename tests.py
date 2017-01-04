from generate import *
from connect import *

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