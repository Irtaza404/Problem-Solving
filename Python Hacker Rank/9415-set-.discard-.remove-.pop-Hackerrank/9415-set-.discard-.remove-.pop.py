n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd=input().split()
    match cmd[0]:
        case "pop":s.pop()
        case "remove":s.remove(int(cmd[1]))
        case "discard":s.discard(int(cmd[1]))
print(sum(s))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna