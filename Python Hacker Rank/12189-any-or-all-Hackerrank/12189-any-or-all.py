n=int(input())
N=list(map(int,input().split()))
if all(i>=0 for i in N):
    print(True if any(j==j[::-1]for j in map(str,N)) else False)
else:
    print(False)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna