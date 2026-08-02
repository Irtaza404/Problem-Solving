# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=input()
loop=False
for i in n:
    if i.isalnum():
        if re.search(rf"{i}{i}",n) is not None:
            loop=True
            break
    else:
        continue

print(i if loop else -1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna