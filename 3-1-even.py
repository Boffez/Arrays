# Array of integers to analyze
arr = [34, 7, 19, 4, 21, 8]

# Initialize a counter for even numbers
even_count = 0
# Initialize an index variable to traverse the array
index = 0

# Loop through the array using the index
while index < len(arr):
    # Check if the current element is even
    if arr[index] % 2 == 0:
        # Increment the even number counter if true
        even_count += 1
    # Move to the next element in the array
    index += 1

# Print the total number of even values in the array
print("Number of even values:", even_count)
