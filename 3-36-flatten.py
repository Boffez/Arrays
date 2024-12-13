# Function to convert a 2D array into a 1D array
def convert_to_1d(array_2d):
    # Use list comprehension to flatten the 2D array into a 1D array
    return [element for row in array_2d for element in row]

# Function to print a 1D array
def print_1d_array(array_1d):
    print(" ".join(map(str, array_1d)))

# Define the 2D arrays
array_1 = [
    [2, 3],
    [1, 5]
]

array_2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array_3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Convert each 2D array into 1D and print the result
print("1D array for the first 2D array:")
array_1d_1 = convert_to_1d(array_1)
print_1d_array(array_1d_1)

print("\n1D array for the second 2D array:")
array_1d_2 = convert_to_1d(array_2)
print_1d_array(array_1d_2)

print("\n1D array for the third 2D array:")
array_1d_3 = convert_to_1d(array_3)
print_1d_array(array_1d_3)
