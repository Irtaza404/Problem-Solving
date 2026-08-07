# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(input().split())
check=True
for _ in range(int(input())):
    if not a>=set(input().split()):
        check=False
        break
print(check)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna