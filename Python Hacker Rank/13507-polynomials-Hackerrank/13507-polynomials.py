import numpy as np

# 1. Read the coefficients as a NumPy array of floats
coefficients = np.array(input().split(), float)

# 2. Read the value of x as a float
x = float(input())

# 3. Evaluate the polynomial at x and print the result
print(np.polyval(coefficients, x))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna