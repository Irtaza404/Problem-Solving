# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word,r=input().split()
r=int(r)
w=sorted(word)


for size in range(1, r + 1):
    for comb in sorted(combinations(w, size)):
        print("".join(comb))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna