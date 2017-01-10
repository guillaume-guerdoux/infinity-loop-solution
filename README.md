# Optimization - Assignment n°1

## Introduction

This repository holds a student program related to the first assignment in optimization ("infinity loop").
The group is formed by Guillaume Guerdoux and Paul de Nonancourt. We used Python 3.5.2. 

## Problem

The problem considered is the one related to the game Infinity Loop. In this game, the user may rotate different kinds of square and has to solve a grid with the following rules: each square has to be connected to others and no branch should be left with nothing at the end.

This is considered as a Constraint satisfaction problem (CSP) and solved as so by using the solver in CentraleSupelec.py written by teacher Christophe Dürr.

### solve_first.py

In this first solver, variables represent whether connectors are present or absent on the four sides of each square.

[1,0,0,0]: connector at the top

[0,1,0,0]: connector to the left

[0,0,1,0]: connector at the bottom

[0,0,0,1]: connector to the right

First, we reduce the domain using unary constraints at the sides of the grid. Then we add binary constraints between squares.

We go through all squares from left to right and from top to bottom. We noticed that with this way, we only have to add constraints between current square and those to its right and bottom (if there are some)

Such program needs some grid formatting and that's why we have functions in useful_functions.py transforming grids to lists and lists to grid

## Useful links

Problem: http://www-desir.lip6.fr/~durrc/Iut/optim/t/dm1-connect
Game associated: https://play.google.com/store/apps/details?id=com.balysv.loop&hl=fr