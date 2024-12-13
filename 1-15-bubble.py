# Bubble sort

def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    # Outer loop for the number of passes
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# List of car fuel consumption data (liters per 100 km)
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print("Original car fuel consumption:", car_fuel_consumption)
#Sort the fuel consumption data
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print("\nOriginal bank transactions:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Sorted bank transactions:", sorted_bank_transactions)
