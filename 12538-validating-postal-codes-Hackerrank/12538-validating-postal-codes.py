# 1. Matches a number between 100000 and 999999
regex_integer_in_range = r"^[1-9]\d{5}$"

# 2. Finds alternating repeating digits (using a lookahead for overlapping)
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna