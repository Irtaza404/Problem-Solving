# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=[]
for _ in range(int(input())):
    n.append(input())
n="\n".join(n)
n=re.sub(r"(?<= )\|\|(?= )","or",n)
n=re.sub(r"(?<= )&&(?= )","and",n)
print(n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna