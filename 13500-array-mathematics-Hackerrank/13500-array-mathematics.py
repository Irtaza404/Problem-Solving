import numpy as np

# 1. Read the dimensions of the arrays
n, m = map(int, input().split())

# 2. Read the elements of array A and array B
# We use a list comprehension to read 'n' lines, split them, and convert to integer arrays
a = np.array([input().split() for _ in range(n)], dtype=int)
b = np.array([input().split() for _ in range(n)], dtype=int)

# 3. Perform and print the element-wise mathematical operations
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a // b)   # Integer Division
print(a % b)    # Modulo
print(a ** b)   # Power


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna