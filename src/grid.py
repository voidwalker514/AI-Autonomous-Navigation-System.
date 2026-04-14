import numpy as np

def create_grid(size):
    return np.zeros((size, size))

def add_obstacles(grid, obstacle_ratio=0.2):
    np.random.seed(42)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if np.random.rand() < obstacle_ratio:
                grid[i][j] = 1
    return grid