from lights_out import lights_out_solver
from matrix_generator import random_matrix_generator


def main():
    matrix = random_matrix_generator(3)
    print("Matriz a resolver")
    print(matrix)
    print("Solución:")
    print(lights_out_solver(matrix))

# poner el coso de __main