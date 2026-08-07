import numpy as np

# 1. Read the two space-separated lines and convert them into 1-D NumPy arrays of integers
a = np.array(input().split(), int)
b = np.array(input().split(), int)

# 2. Compute and print the inner product
print(np.inner(a, b))

# 3. Compute and print the outer product
print(np.outer(a, b))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna