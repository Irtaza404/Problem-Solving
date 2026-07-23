# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split()))
n=int(input())
for _ in range(n):
    name=input().split()
    b=set(map(int,input().split()))
    match name[0]:
        case "update":a|=b
        case "intersection_update":a&=b
        case "symmetric_difference_update":a^=b
        case "difference_update":a-=b

print(sum(a))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna