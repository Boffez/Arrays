# Function to count occurrences of a value in a tuple
def count_occurrences(tup, value):
    return tup.count(value)

# Sample tuple and value to search for
my_tuple = (50, 20, 40, 50, 30, 50)
value_to_count = 50

# Count the occurrences of the value in the tuple
occurrences = count_occurrences(my_tuple, value_to_count)

# Print the result
print(f"Tuple: {my_tuple}")
print(f"Value: {value_to_count}")
print(f"Number of occurrences: {occurrences}")
