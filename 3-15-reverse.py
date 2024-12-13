# Program to print a tuple in reverse order

# Define the tuple
tuple_data = (10, 20, 30, 40, 50)

# Print the original tuple
print("Tuple:", ",".join(map(str, tuple_data)))

# Reverse the tuple
reversed_tuple = tuple_data[::-1]

# Print the reversed tuple
print("Reverse order:", ",".join(map(str, reversed_tuple)))
