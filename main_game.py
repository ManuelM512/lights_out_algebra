import pygame
from game.button import Button
from game.colors import BLACK, WHITE
from game.grid import Grid
from lights_out import lights_out_solver
from matrix_generator import random_matrix_generator

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 700
GRID_SIZE = 10
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
BUTTON_HEIGHT = 80
PADDING = 10

# Pygame Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lights Out")
font = pygame.font.Font(None, 100)
win_text = font.render("You Win!", True, WHITE)
win_text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


class Game:
    def __init__(self, matrix, solution):
        self.grid = Grid(len(matrix), CELL_SIZE, PADDING, matrix, solution)
        self.button = Button(
            (SCREEN_WIDTH - CELL_SIZE * 2) // 2.5,
            SCREEN_HEIGHT - BUTTON_HEIGHT - PADDING,
            CELL_SIZE * 4,
            BUTTON_HEIGHT,
            "Highlight Solution",
        )
        self.highlight_active = False
        self.running = True
        self.win = False

    def draw(self):
        """Draws all game elements."""
        screen.fill(BLACK)
        self.grid.draw(screen)
        self.button.draw(screen)
        if self.highlight_active:
            self.grid.highlight_solution(screen)

    def handle_click(self, pos):
        """Handles clicks on the grid and button."""
        x, y = pos
        if y < SCREEN_HEIGHT - BUTTON_HEIGHT - PADDING:
            row, col = y // CELL_SIZE, x // CELL_SIZE
            self.grid.solution[row][col] = 0
            self.grid.toggle_cell(row, col)
        elif self.button.is_clicked(pos):
            self.highlight_active = not self.highlight_active

    def run(self):
        """Main game loop."""

        while self.running:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.win:
                    self.handle_click(event.pos)
                    if not self.grid.grid.sum():
                        self.win = True

            if self.win:
                screen.blit(win_text, win_text_rect)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    matrix = random_matrix_generator(10)
    solution = lights_out_solver(matrix)
    game = Game(matrix, solution)
    game.run()
