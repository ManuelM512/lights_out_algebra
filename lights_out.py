import numpy as np
from array_utils import get_solution_array
from matrix_utils import binary_gaussian_elimination, get_neighbors_matrix


def lights_out_solver(matrix: np.ndarray[np.ndarray]) -> np.ndarray:
    """Solver algorithm for the lights out game.

    Args:
        matrix (np.ndarray[np.ndarray]): NxN matrix composed of 0's and 1's.

    Returns:
        np.ndarray: The solution array for the game.
    """
    # Turn the matrix into an array-like, as it will be the last column of the matrix to solve
    matrix_2_array = matrix.reshape(-1)
    # Generate the matrix that represents by what each light is affected
    neighbors_matrix = get_neighbors_matrix(len(matrix))
    # Concatenate the array of the given matrix to the light-affecting matrix
    matrix_to_solve = np.hstack([neighbors_matrix, matrix_2_array.reshape(-1, 1)])
    solved_matrix = binary_gaussian_elimination(matrix_to_solve)
    return get_solution_array(solved_matrix)
