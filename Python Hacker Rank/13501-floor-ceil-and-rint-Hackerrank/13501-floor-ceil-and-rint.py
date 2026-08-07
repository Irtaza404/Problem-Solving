import numpy as np

# This line is REQUIRED to pass HackerRank's strict output formatting
np.set_printoptions(legacy='1.13')

# 1. Read the input string, split it by spaces, and convert to a float array
my_array = np.array(input().split(), float)

# 2. Print the three mathematical operations
print(np.floor(my_array))
print(np.ceil(my_array))
print(np.rint(my_array))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna