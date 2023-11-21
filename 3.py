import time
import pygame
import numpy as np

# Define colors
color_bg = (0, 0, 0)  # Black
color_alive = (255, 255, 0)  # White

# Define grid size and cell size
grid_size = (100, 150)
cell_size = 10

# Function to initialize the grid randomly
def initialize_grid():
    return np.random.choice([0, 1], size=grid_size, p=[0.5, 0.5])

# Function to update the grid based on the game rules
def update_grid(grid):
    new_grid = np.copy(grid)
    for row in range(1, grid.shape[0] - 1):
        for col in range(1, grid.shape[1] - 1):
            neighbors = np.sum(grid[row - 1:row + 2, col - 1:col + 2]) - grid[row, col]
            
            if grid[row, col] == 1:  # Live cell
                if neighbors < 2 or neighbors > 3:
                    new_grid[row, col] = 0
            else:  # Dead cell
                if neighbors == 3:
                    new_grid[row, col] = 1
    return new_grid

# Function to draw the grid on the Pygame screen
def draw_grid(screen, grid):
    screen.fill(color_bg)
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            color = color_alive if grid[row, col] == 1 else color_bg
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size - 1, cell_size - 1))

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((grid_size[1] * cell_size, grid_size[0] * cell_size))

    # Initialize the grid
    grid = initialize_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(screen, grid)
        grid = update_grid(grid)

        pygame.display.flip()
        time.sleep(0.1)

    pygame.quit()

if __name__ == "_main_":
    main()