# Function to check if arr1 is a subset of arr2
def is_subset(arr1, arr2):
    # Convert arr2 to a set for faster lookup
    set_arr2 = set(arr2)
    
    # Check if all elements of arr1 are in arr2
    for element in arr1:
        if element not in set_arr2:
            return False
    return True

# Example arrays
arr1 = [3, 7, 1]
arr2 = [7, 3, 1, 4, 8, 2]

# Check if arr1 is a subset of arr2
if is_subset(arr1, arr2):
    print("arr1 is a subset of arr2.")
else:
    print("arr1 is not a subset of arr2.")
