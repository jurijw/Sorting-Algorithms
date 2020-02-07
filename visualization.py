from random import randrange
import numpy as np
import pygame
import sys

# Constants
size = width, height = 1000, 500
user_in = {"num_cells": 100, "low": 0, "high": 100, "method": "bubble"}
num_cells = 100
# Colors
white = 255, 255, 255
black = 0, 0, 0
red = 255, 100, 100
green = 100, 255, 100
blue = 100, 100, 255


class Cell:
    def __init__(self, val, pos):
        self.pos = pos
        self.val = val
        # Properties for visualization
        self.current = False
        self.neighbor = False

    def __repr__(self):
        return f"Cell({self.val}, {self.pos})"


def initialize_cell_array(user_in):
    """
    Initializes an array of n objects of type Cell. Gives each cell
    a random value in the user specified range.
    Args:
    user_in -> Dict
    Returns:
    cell_array -> numpy.ndarray[Cell]
    """
    # Get relevant user input
    n = user_in["num_cells"]
    low = user_in["low"]
    high = user_in["high"]

    # Placeholder array
    cell_array = np.zeros(n, dtype=Cell)

    # Get n random integer value between the bounds
    values = np.random.randint(low, high + 1, (n))

    # Populate the array
    for i, val in enumerate(values):
        cell_array[i] = Cell(val, i)

    return cell_array


def display_cells(screen, cell_array, user_in):
    """
    Takes a screen object and an array of cells and displays
    them on a screen object in the correct position and a height
    corresponding to their value as a fraction of the max value. 
    Args:
    screen -> pygame.Surface
    cell_array -> numpy.ndarray[Cell]
    user_in -> Dict
    Returns:
    None
    """

    # Get relevant user input
    n = user_in["num_cells"]
    high = user_in["high"]

    # Get info about screen size
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Determine width of screen alottet per cell
    width_per_cell = screen_width // n

    cell_width_scale = 0.9  # Fraction of alottet space per cell to be used
    cell_width = cell_width_scale * width_per_cell

    # Fill the background of the screen
    screen.fill(white)
    for i, cell in enumerate(cell_array):
        # Determine location of rectangle for the cell
        offset_x = (1 - cell_width_scale) // 2 * width_per_cell
        cell_x = i * width_per_cell + offset_x
        # Determine cell height as a fraction of screen height
        cell_height = screen_height // high * cell.val
        cell_y = screen_height - cell_height

        # Determine color
        color = black
        if cell.current:
            color = green
        elif cell.neighbor:
            color = blue

        # Draw a bar corresponding to the value of the cell
        pygame.draw.rect(screen, color, ((cell_x, cell_y), (cell_width, cell_height)))


def bubble_sort(screen, cell_array, user_in, accelerated=True):
    """
    Applies bubble sort onto an array of Cell objects.
    Modifies the array itself. Takes an accelerated argument, 
    which speeds up the bubble sort by taking advantage of the 
    fact that the last n elements will always be sorted after the
    nth run through. Set to True by default.

    Args:
    screen -> pygame.Surface
    cell_array -> numpy.ndarray[Cell]
    user_in -> Dict
    accelerated -> Bool
    Returns:
    True when completed
    """
    n = len(cell_array)
    swapped = True
    while swapped:
        swapped = False

        for i in range(n - 1):
            current = cell_array[i]
            neighbor = cell_array[i + 1]
            # Set some cell properties for visualization
            current.current = True
            neighbor.neighbor = True

            # Compare two neighbors and swap if neccessary
            if current.val > neighbor.val:
                current.val, neighbor.val = neighbor.val, current.val
                swapped = True

            display_cells(screen, cell_array, user_in)
            pygame.display.update()

            current.current = False
            neighbor.neighbor = False

        if accelerated:
            n -= 1

    # Return true when the sort is complete.
    return True


def merge_sort(screen, cell_array):

    # Base case - list is of length 1 (cannot be spiit further)
    if len(cell_array) <= 1:
        return cell_array

    # Recursive case - split the array into two
    else:
        left = np.array([], dtype=Cell)
        right = np.array([], dtype=Cell)
        for i, cell in enumerate(cell_array):
            if i < len(cell_array) // 2:
                left = np.append(left, cell)  # FIX: get equivalent method for numpy arrays
            else:
                right = np.append(right, cell)

        # Recursive call to sort sublists
        left = merge_sort(screen, left)
        right = merge_sort(screen, right)

        # Return the two concatenated arrays
        return np.concatenate((left, right))


def main():
    # Setup screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Sorting Visualization")

    # Initialize cell array
    cell_array = initialize_cell_array(user_in)

    terminated = False
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # if(bubble_sort(screen, cell_array, user_in)):
        #     print("Finished bubble sort!")
        #     # Await new user inputs

        merge_sort(screen, cell_array)

        # Draw the screen
        display_cells(screen, cell_array, user_in)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
