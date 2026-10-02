import numpy as np


def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    columns = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter the elements of {name} row by row:")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        while len(row) != columns:
            print(f"Please enter exactly {columns} values.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))

        matrix.append(row)

    return np.array(matrix)


def display_matrix(matrix):
    print("\nResult:")
    print(matrix)


def matrix_addition():
    print("\n--- Matrix Addition ---")

    matrix_a = input_matrix("Matrix A")
    matrix_b = input_matrix("Matrix B")

    if matrix_a.shape != matrix_b.shape:
        print("\nError: Both matrices must have the same dimensions.")
        return

    result = np.add(matrix_a, matrix_b)
    display_matrix(result)


def matrix_subtraction():
    print("\n--- Matrix Subtraction ---")

    matrix_a = input_matrix("Matrix A")
    matrix_b = input_matrix("Matrix B")

    if matrix_a.shape != matrix_b.shape:
        print("\nError: Both matrices must have the same dimensions.")
        return

    result = np.subtract(matrix_a, matrix_b)
    display_matrix(result)


def matrix_multiplication():
    print("\n--- Matrix Multiplication ---")

    matrix_a = input_matrix("Matrix A")
    matrix_b = input_matrix("Matrix B")

    if matrix_a.shape[1] != matrix_b.shape[0]:
        print(
            "\nError: Number of columns in Matrix A "
            "must equal number of rows in Matrix B."
        )
        return

    result = np.matmul(matrix_a, matrix_b)
    display_matrix(result)


def matrix_transpose():
    print("\n--- Matrix Transpose ---")

    matrix = input_matrix("Matrix")

    result = np.transpose(matrix)
    display_matrix(result)


def matrix_determinant():
    print("\n--- Matrix Determinant ---")

    matrix = input_matrix("Matrix")

    if matrix.shape[0] != matrix.shape[1]:
        print("\nError: Determinant can only be calculated for a square matrix.")
        return

    result = np.linalg.det(matrix)

    print(f"\nDeterminant: {result:.2f}")


def main():
    while True:
        print("\n========================================")
        print("       MATRIX OPERATIONS TOOL")
        print("========================================")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Matrix Determinant")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            matrix_addition()

        elif choice == "2":
            matrix_subtraction()

        elif choice == "3":
            matrix_multiplication()

        elif choice == "4":
            matrix_transpose()

        elif choice == "5":
            matrix_determinant()

        elif choice == "6":
            print("\nThank you for using Matrix Operations Tool!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()