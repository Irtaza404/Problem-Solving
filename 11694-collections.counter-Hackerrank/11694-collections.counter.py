# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
total=0
sizes=Counter(map(int,input().split()))
for _ in range(int(input())):
    size,price=list(map(int,input().split()))
    if sizes.get(size,0)>0:
        total+=price
        sizes[size]=sizes.get(size)-1
print(total)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna