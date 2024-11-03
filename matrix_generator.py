from random import randint

import numpy as np


def random_matrix_generator(n: int) -> np.ndarray[np.ndarray]:
    """Generates a matrix of nxn, composed of 0's and 1's randomly located.

    Args:
        n (int): Length of the matrix, being it a matrix of nxn

    Returns:
        np.ndarray[np.ndarray]: Matrix composed of 0's and 1's
    """
    matrix = np.zeros((n, n), dtype=int)
    amount_lights_on = randint((n**2) // 8, n**2)
    lights_coordinates = set()
    while len(lights_coordinates) < amount_lights_on:
        coord = (randint(0, n - 1), randint(0, n - 1))
        if coord not in lights_coordinates:
            matrix[coord[0], coord[1]] = 1
            lights_coordinates.add(coord)
    return matrix
