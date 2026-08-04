import re

# The regular expression pattern
regex_pattern = r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})\b"

# Read the number of lines
for _ in range(int(input())):
    line = input()
    
    # Find all matches in the current line
    matches = re.findall(regex_pattern, line)
    
    # Print each matched color code
    for match in matches:
        print(match)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna