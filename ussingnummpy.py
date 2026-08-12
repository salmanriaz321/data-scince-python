import numpy as np

# 1. Create an array consisting of linearly spaced elements between 0 to 9
# Note: Since the next questions imply integers (odd/even), we create 10 integer steps.
original_array = np.linspace(0, 9, 10, dtype=int)
print("1. Original Array:", original_array)

# 2. Replace all odd numbers with -1 without modifying the original array
modified_array = np.where(original_array % 2 != 0, -1, original_array)
print("2. Modified Array (odds replaced):", modified_array)
print("   Verification of Original Array:", original_array)

# 3. Convert the original 1-dimensional array into a 2-dimensional array with two rows
two_d_array = original_array.reshape(2, 5)
print("3. 2D Array (2 rows):\n", two_d_array)

# 4. Iterate through the original array and find out sum of all evens
# Note: The problem contains a typo "events", which logically means "even numbers".
even_sum = 0
for element in original_array:
    if element % 2 == 0:
        even_sum += element
print("4. Sum of all even numbers:", even_sum)
