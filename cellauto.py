import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def count_live_neighbors(grid, x, y, N):
    # Define the relative positions of the eight neighbors
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),         (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    
    numNeighbors = 0
    for dx, dy in neighbors:
        # Calculate neighbor's position with wrapping
        nx, ny = (x + dx) % N, (y + dy) % N
        numNeighbors += grid[nx, ny]
    
    return numNeighbors

# Updates grid for each frame
def update(frameNum, img, grid, N):

    # Create copy of grid to store updates
    newGrid = grid.copy()

    for i in range(N):
        for j in range(N):
            numNeighbors = count_live_neighbors(grid, i, j, N)
            
            if grid[i, j] == 1:         # Cell rules
                if (numNeighbors < 2) or (numNeighbors > 3):
                    newGrid[i, j] = 0   # Cell dies
            else:                       # Cell becomes alive
                if numNeighbors == 3:
                    newGrid[i, j] = 1

    img.set_data(newGrid)           # Update image data
    grid[:] = newGrid[:]            # Update the grid
    return img,

N = 50                # Grid size     
grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)    # Init Grid with rand vals (0 or 1)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')

ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),frames=10, interval=50, save_count=50) # Create the animation

plt.show()      # Display
