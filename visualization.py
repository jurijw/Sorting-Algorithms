from random import randrange
import numpy as np
import pygame
import sys

# Constants
size = width, height = 1000, 500
num_cells = 100

def initialize_cell_array(n, low=0, high=100):
    """
    Initializes an array of n objects of type Cell. Gives each cell
    a random value in the specified range (default 0-100).
    Args:
    n -> Int
    Returns:
    cell_array -> numpy.ndarray[Cell]
    """
    # Placeholder array
    cell_array = np.zeros(n, dtype=Cell)

    # Get n random integer value between the bounds
    values = np.random.randint(low, high+1, (n))

    # Populate the array
    for i, val in enumerate(values):
        cell_array[i].pos = i
        cell_array[i].val = val
        
    return cell_array

class Cell:
    def __init__(self, val, pos):
        self.pos = pos
        self.val = val

    def __repr__(self):
        return f"Cell({self.val}, {self.pos})"

def main():
    # Setup screen 
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sorting Visualization")

    # Initialize cell array
    cell_array = initialize_cell_array(n=100, low=0, high=100)

    terminated = False
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

if __name__ == "__main__":
    pygame.init()
    main()