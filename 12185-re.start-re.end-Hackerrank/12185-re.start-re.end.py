# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
data=input()
n=input()
check=False
for i in re.finditer(rf"(?={re.escape(n)})",data):
    print((i.start(),i.start() + len(n) - 1))
    check=True

if not check :
    print((-1,-1))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna