import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# --- ADD YOUR CODE BELOW THIS LINE ---

# 1. Read the matrix column by column using a list comprehension
decoded_string = "".join([matrix[row][col] for col in range(m) for row in range(n)])

# 2. Use Regex Lookaround to replace symbols between alphanumeric characters
# The problem strictly defines alphanumeric as a-z, A-Z, 0-9 (meaning underscores are symbols)
pattern = r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])"

# 3. Print the cleanly substituted string
print(re.sub(pattern, " ", decoded_string))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna