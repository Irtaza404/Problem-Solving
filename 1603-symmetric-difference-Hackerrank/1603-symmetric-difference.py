# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
for num in sorted(a^b):
    print(num) 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna