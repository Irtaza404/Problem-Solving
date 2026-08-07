import numpy as np

# 1. Read dimensions
n, m = map(int, input().split())

# 2. Build the array
my_array = np.array([input().split() for _ in range(n)], int)

# 3. Print mean and var normally (modern NumPy handles the spaces correctly now)
print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))

# 4. Round the std to exactly 11 decimal places
print(round(np.std(my_array), 11))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna