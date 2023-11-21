import pygame
import numpy as np

# Constants
GRID_SIZE = 50
CELL_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize grid randomly
grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE))

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
pygame.display.set_caption("Conway's Game of Life")

# Function to count live neighbors for a given cell
def count_neighbors(x, y):
    neighbors = [
        grid[i, j]
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and (i != x or j != y)
    ]
    return sum(neighbors)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Copy the current grid to avoid updating in-place
    new_grid = grid.copy()

    # Update the grid based on the rules
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = count_neighbors(i, j)

            if grid[i, j] == 1:  # Live cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0  # Dies
            else:  # Dead cell
                if neighbors == 3:
                    new_grid[i, j] = 1  # Comes to life

    grid = new_grid

    # Draw the grid
    screen.fill(BLACK)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(
                screen, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    pygame.display.flip()
    pygame.time.delay(100)  # Adjust the delay as needed
