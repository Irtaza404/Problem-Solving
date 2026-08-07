import numpy as np

# 1. Read the dimensions N (rows) and M (columns)
n, m = map(int, input().split())

# 2. Read the matrix and convert it into a NumPy array of integers
my_array = np.array([input().split() for _ in range(n)], int)

# 3. Find the minimum values along axis 1 (across the rows)
min_array = np.min(my_array, axis=1)

# 4. Find and print the maximum value of the resulting array
print(np.max(min_array))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna