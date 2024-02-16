#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

max_product = 0

for i in range(20):
    for j in range(20):
        if j+3<20:
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            max_product = max(max_product, product)
        
        if i+3<20:
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            max_product = max(max_product, product)
            
        if i+3<20 and j+3<20:
            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            max_product = max(max_product, product)
            
        if i+3<20 and j-3>=0:
            product = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
            max_product = max(max_product, product)
            
print(max_product)
