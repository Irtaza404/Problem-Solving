import numpy as np

# 1. Read the dimensions N (rows) and M (columns)
n, m = map(int, input().split())

# 2. Read the matrix and convert it into a NumPy array of integers
my_array = np.array([input().split() for _ in range(n)], int)

# 3. Sum the array over axis 0 (summing down the columns)
sum_array = np.sum(my_array, axis=0)

# 4. Calculate and print the product of the summed array
print(np.prod(sum_array))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna