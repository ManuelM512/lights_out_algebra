import numpy as np


def get_solution_array(matrix: np.ndarray[np.ndarray]) -> np.ndarray[np.ndarray]:
    """Returns the last column of a matrix, as it will be the solution array.

    Args:
        matrix (np.ndarray[np.ndarray]): NxN matrix, of 0's and 1's.

    Returns:
        np.ndarray[np.ndarray]: Array with 1's in the x(i)'s lights to press to solve the game.
    """
    n = len(matrix)
    solution_array = np.zeros(n, dtype=int)
    for i in range(n):
        solution_array[i] = matrix[i][n]
    return solution_array


def prettier_result(result_array: np.ndarray) -> list[list[int]]:
    n = int(len(result_array) ** (1 / 2))
    pretty_result = result_array.reshape(n, n)
    return pretty_result
