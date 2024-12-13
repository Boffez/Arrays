# Function to transpose a matrix
def transpose_matrix(m):
    # Transpose the matrix by converting rows to columns
    return [list(row) for row in zip(*m)]

# Function to print a 2D array in rows and columns
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Define the matrices
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix_3 = [
    [5, 6, 7, 8]
]

# Print the transposed matrices
print("Transpose of matrix 1:")
transposed_1 = transpose_matrix(matrix_1)
print_matrix(transposed_1)

print("\nTranspose of matrix 2:")
transposed_2 = transpose_matrix(matrix_2)
print_matrix(transposed_2)

print("\nTranspose of matrix 3:")
transposed_3 = transpose_matrix(matrix_3)
print_matrix(transposed_3)
