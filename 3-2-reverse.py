# Given array of natural numbers
array = [15, 8, 31, 47, 2, 19]

# Print the original array
print("Existed array:", end=" ")
for num in array:
    print(num, end=" ")


print("\nReverse array:", end=" ")
for i in range(len(array) - 1, -1, -1):
    print(array[i], end=" ")
