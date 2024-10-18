from array_utils import prettier_result
from lights_out import lights_out_solver
from matrix_generator import random_matrix_generator


def main():
    matrix = random_matrix_generator(3)
    print("Matriz a resolver")
    print(matrix)
    print("\nArray de solución:")
    solution_array = lights_out_solver(matrix)
    print(solution_array)
    print("\nSolución estilizada para ver mejor qué botones apretar:")
    print(prettier_result(solution_array))


if __name__ == "__main__":
    main()
