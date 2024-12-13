# Function to check if a number is present in an array
def occurs(number, array):
    # Return True if the number is found in the array, otherwise False
    return number in array

# Main program
if __name__ == "__main__":
    # Define the array to check
    array = [15, 38, 7, 23, 14]

    # Prompt the user to enter a number
    number = int(input("Enter a number: "))

    # Display the array
    print("Array:", " ".join(map(str, array)))

    # Check if the number is in the array and display the result
    if occurs(number, array):
        print(f"Result: number {number} appears in the array")
    else:
        print(f"Result: number {number} does not appear in the array")
