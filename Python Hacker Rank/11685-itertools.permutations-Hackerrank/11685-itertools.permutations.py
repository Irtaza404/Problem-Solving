# Enter your code here. Read input from STDIN. Print output to STDOUT
i=input().split()

from itertools import permutations

for i in sorted(list(permutations(i[0],int(i[1])))):
    print("".join(i))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna