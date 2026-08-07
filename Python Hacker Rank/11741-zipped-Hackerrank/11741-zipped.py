# Enter your code here. Read input from STDIN. Print output to STDOUT
N,n=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(float,input().split())))

for i in zip(*l):
    print(f"{sum(i)/n:.1f}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna