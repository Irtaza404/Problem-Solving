# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s=input()
for key,group in groupby(s):
    print((len(list(group)), int(key)), end=" ")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna