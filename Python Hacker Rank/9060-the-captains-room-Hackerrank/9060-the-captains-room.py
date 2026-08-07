# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
seen = set()
duplicates = set()
for num in input().split():
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("".join(seen-duplicates))



















# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna