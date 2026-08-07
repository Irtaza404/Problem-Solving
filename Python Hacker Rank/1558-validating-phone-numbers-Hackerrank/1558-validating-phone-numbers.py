# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    number=input()
    if re.search(r"^(9|8|7)\d{9}$",number):
        print("YES")
    else:
        print("NO")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna