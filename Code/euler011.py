# Project Euler 11: Largest product in a grid
# Dated: 2021-10-16

import sys

def largest_product(grid):
    largest = 0
    for i in range(20):
        for j in range(20):
            product_right = grid[i][j]
            product_down  = grid[i][j]
            product_diag_right  = grid[i][j]
            product_diag_left   = grid[i][j]
            for k in range(1,4):
                if j+k < 20:
                    product_right *= grid[i][j+k]
                if i+k < 20:
                    product_down *= grid[i+k][j]
                if i+k < 20 and j+k < 20:
                    product_diag_right *= grid[i+k][j+k]
                if i-k < 20 and j+k < 20:
                    product_diag_left  *= grid[i-k][j+k]
            largest = max(product_diag_right, product_diag_left, product_down, product_right,largest)
    return largest

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
print(largest_product(grid))
