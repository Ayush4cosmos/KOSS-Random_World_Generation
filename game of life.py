import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Count neighbors
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            # Apply rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Constants
ON = 255
OFF = 0
N = 100
updateInterval = 50

# Create a grid of N x N random values
grid = np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

# Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N,),
                              frames=10,
                              interval=updateInterval,
                              save_count=50)

plt.show()
