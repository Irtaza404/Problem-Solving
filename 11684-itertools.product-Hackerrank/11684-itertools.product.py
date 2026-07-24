# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=map(int,input().split())
b=map(int,input().split())
for p in list(product(a,b)): 
    print(p,end=" ")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna