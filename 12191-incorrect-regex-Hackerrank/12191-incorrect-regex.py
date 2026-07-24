# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(raw_input())):
    try:    
        re.compile(raw_input().strip())
        print(True)
    except re.error:
        print(False)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna