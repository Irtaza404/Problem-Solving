# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter 
l=[]
for _ in range(int(input())):
   l.append(input())
l=Counter(l).values()
print(len(l))
for w in l:
    print(w,end=" ")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna