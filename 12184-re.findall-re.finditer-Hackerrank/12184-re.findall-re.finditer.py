# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m=re.findall( r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])",input())
if m:
    for i in m:
        print(i)
else:
    print(-1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna