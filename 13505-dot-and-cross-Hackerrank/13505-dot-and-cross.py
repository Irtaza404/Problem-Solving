import numpy as np

# 1. Read the dimension N (since it's an N x N matrix, we only get one number)
n = int(input())

# 2. Read the next N lines for Matrix A
a = np.array([input().split() for _ in range(n)], int)

# 3. Read the next N lines for Matrix B
b = np.array([input().split() for _ in range(n)], int)

# 4. Compute and print the matrix multiplication (dot product)
print(np.dot(a, b))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna