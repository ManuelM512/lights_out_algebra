import numpy as np
import pygame

from game.colors import DARK_GREEN, GRAY, WHITE


class Grid:
    def __init__(self, grid_size, cell_size, padding, matrix, solution):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.padding = padding
        self.grid = matrix
        self.solution = solution.reshape(10, 10)

    def draw(self, surface):
        """Draws the grid with colors based on cell values."""
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                color = WHITE if self.grid[row][col] == 1 else GRAY
                pygame.draw.rect(
                    surface,
                    color,
                    (
                        col * self.cell_size + self.padding,
                        row * self.cell_size + self.padding,
                        self.cell_size - self.padding,
                        self.cell_size - self.padding,
                    ),
                )

    def toggle_cell(self, row, col):
        """Toggles the cell at (row, col) and its neighbors."""
        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            self.grid[row][col] ^= 1
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= r < self.grid_size and 0 <= c < self.grid_size:
                self.grid[r][c] ^= 1

    def highlight_solution(self, surface):
        """Highlights cells in the solution matrix."""
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.solution[row][col] == 1:
                    pygame.draw.rect(
                        surface,
                        DARK_GREEN,
                        (
                            col * self.cell_size + self.padding,
                            row * self.cell_size + self.padding,
                            self.cell_size - self.padding,
                            self.cell_size - self.padding,
                        ),
                        4,
                    )
