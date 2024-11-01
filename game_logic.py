# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (150, 150, 150)
DARK_GREEN = (34, 139, 34)


class GameLogic:
    def __init__(self, board):
        self.width, self.height = 600, 650  # Additional space for the button
        self.board = board
        self.click_counter = 0
        self.grid_size = len(board[0])
        self.rows, self.cols = len(board[0])
        self.cell_size = self.width // self.cols

    def toggle_highlight_solution(self):
        pass

    # Function to draw grid and button

    def draw_grid(highlight_cells=[]):
        pass
