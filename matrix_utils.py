import numpy as np


def binary_gaussian_elimination(
    matrix: np.ndarray[np.ndarray],
) -> np.ndarray[np.ndarray]:
    """Gaussian elimination applied in a matrix composed of 0's and 1's.

    Args:
        matrix (np.ndarray[np.ndarray]): Matrix of NxN length composed of 0's and 1's.

    Returns:
        np.ndarray[np.ndarray]: Matrix with transformations applied.
    """
    # As a summary, this will make all the cells not in the diagonal to be 0's, by applying a
    # binary sum (XOR). This will be done in ascending order by columns, to make the current cell
    # of the diagonal to be the only 1 of the column
    n = len(matrix)
    for i in range(n):
        if not matrix[i][i]:
            for j in range(i + 1, n):
                # This works as a swap of rows, to have a 1 in the position it's needed to be
                if matrix[j][i]:
                    matrix[i] ^= matrix[j]
                    matrix[j] ^= matrix[i]
                    matrix[i] ^= matrix[j]
                    break
        for i_sub in range(0, n):
            # For each cell of the diagonal, makes all the other cells in the same column to be 0
            # by applying an XOR operation on the selected row (sub_i) with the current row (i)
            if i_sub != i:
                if matrix[i_sub][i]:
                    matrix[i_sub] ^= matrix[i]
    return matrix


def get_neighbors_matrix(n: int) -> np.ndarray:
    """Generates an NxN matrix, with 1's in the position that affects each light (row).

    Args:
        n (int): Length of the matrix.

    Returns:
        np.ndarray: NxN matrix.
    """
    matrix = []
    # For each light, will make it's own array, with 1's in the position of the lights that
    # affect the current light. Then it will append the array into the matrix to be returned
    for i in range(n**2):
        base_array = np.zeros(n**2, dtype=int)
        base_array[i] = 1
        if i + n < n**2:
            base_array[i + n] = 1
        if (i + 1) % n != 0:
            base_array[i + 1] = 1
        if i - n >= 0:
            base_array[i - n] = 1
        if i % n != 0:
            base_array[i - 1] = 1
        matrix.append(base_array)
    return matrix
