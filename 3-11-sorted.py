arrays = [
    [64, 34, 25, 12, 22, 11, 90], 
    [5, 2, 9, 1, 7, 6, 3],         
    [38, 27, 43, 3, 9, 82, 10]    
]

# Function to perform bubble sort on a given array
def bubblesort(arr):
    # Get the length of the array
    n = len(arr)
    # Outer loop for the number of passes
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # Return the sorted array
    return arr

# Main function to process and sort each array
def main():
    for arr in arrays:
        # Print the original array
        print(f"Original: {arr}")
        # Print the sorted array
        print(f"Sorted:   {bubblesort(arr)}\n")
    
# Check if the script is run directly
if __name__ == '__main__':
    main()
