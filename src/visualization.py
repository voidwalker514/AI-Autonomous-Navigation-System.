import matplotlib.pyplot as plt
import numpy as np

def animate(grid, path, start, goal):
    plt.ion()
    fig, ax = plt.subplots()

    for i in range(len(path)):
        ax.clear()
        ax.imshow(grid, cmap='gray')

        # Path till now
        for (x, y) in path[:i+1]:
            ax.scatter(y, x)

        # Start & goal
        ax.scatter(start[1], start[0])
        ax.scatter(goal[1], goal[0])

        plt.pause(0.2)

    plt.ioff()
    plt.show()