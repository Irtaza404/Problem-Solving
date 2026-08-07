# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    n=input()
    a=set(input().split())
    m=input()
    b=set(input().split())
    print(a.issubset(b))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna