# Define the array
array = [8, 2, 5, 1, 9]

# Compute the second power (square) of each element
squared_array = [x**2 for x in array]

# Print the original array and the squared values
print("Array:", " ".join(map(str, array)))
print("2nd power:", " ".join(map(str, squared_array)))
