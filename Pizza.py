#pizza

import math

#Constants
slices = 8
family_size = 4

#Input
slices = int(input('How many slices does each person eat?'))

#Math
total = slices * family_size
pizzas = math.ceil(total / slices)
whole_pizzas = total // slices
remain = total % slices

#Leftovers
leftovers = (slices - remain) % slices

#Output
print('Whole pizzas needed:', total)
print('Pizza slices left over:', pizzas)
