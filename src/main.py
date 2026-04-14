from grid import *
from astar import *
from simulation import *
from visualization import *

grid = create_grid(20)
grid = add_obstacles(grid)

start = (0, 0)
goal = (19, 19)

# Ensure start/goal are free
grid[start] = 0
grid[goal] = 0

path = astar(grid, start, goal)

if not path:
    print("No path found!")
else:
    simulate_movement(path)
    animate(grid, path, start, goal)