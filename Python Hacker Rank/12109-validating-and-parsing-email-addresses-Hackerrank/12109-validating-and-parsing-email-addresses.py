import re
import email.utils

# 1. Define the regex pattern based on the strict criteria
regex_pattern = r"^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

# 2. Loop through the number of inputs
for _ in range(int(input())):
    # Read the raw input line
    raw_input = input()
    
    # 3. Parse the name and email out of the raw string
    parsed_name, parsed_email = email.utils.parseaddr(raw_input)
    
    # 4. Check if the parsed email matches our regex rules
    if re.match(regex_pattern, parsed_email):
        # 5. If valid, format it back into 'name <email>' and print
        print(email.utils.formataddr((parsed_name, parsed_email)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna