class GameBoard:
    def __init__(self, matrix: list[list]):
        self.matrix_board = matrix
        self.solution_matrix = []
        self.tiles_on_color = (255, 255, 0)
        self.tiles_off_color = (50, 50, 50)
        self.tiles_highlight_color = (0, 255, 0)
        self.highlight_solution = False
        self.rendered_matrix = matrix.copy()
        # BUTTON_COLOR = (100, 100, 250)
        # BUTTON_HIGHLIGHT_COLOR = (150, 150, 255)
        # TEXT_COLOR = (255, 255, 255)

    def change_palette():
        pass

    def set_solution(self, solution_matrix: list[list]):
        self.solution_matrix = solution_matrix

    def toggle_highlight_solution():
        pass

    def toggle_cells(self, row, col):
        self.matrix_board = []
        if (
            row >= 0
            and row < len(self.matrix_board)
            and col >= 0
            and col < len(self.matrix_board)
        ):
            self.matrix_board[row][col] = 1 - self.matrix_board[row][col]
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= r < len(self.matrix_board) and 0 <= c < len(self.matrix_board):
                self.matrix_board[r][c] = 1 - self.matrix_board[r][c]
