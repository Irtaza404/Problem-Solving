import numpy as np

# 1. Read the dimension N of the NxN matrix
n = int(input())

# 2. Read the matrix and convert it into a NumPy array of floats
# (We use floats because determinants often deal with decimal values)
matrix = np.array([input().split() for _ in range(n)], float)

# 3. Calculate the determinant using the linalg (Linear Algebra) submodule
determinant = np.linalg.det(matrix)

# 4. Print the result rounded to 2 decimal places to pass the strict test cases
print(round(determinant, 2))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna