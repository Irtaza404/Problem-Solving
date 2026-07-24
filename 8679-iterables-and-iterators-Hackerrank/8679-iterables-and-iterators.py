# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=int(input())
N=input().split()
k=int(input())
N=list(combinations(N,k))
coun=0
for c in N:
    if "a" in c:
        coun+=1
print(coun/len(N))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna