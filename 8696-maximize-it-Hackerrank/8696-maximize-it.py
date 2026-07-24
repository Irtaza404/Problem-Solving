# Enter your code here. Read input from STDIN. Print output to STDOUT
K,M=list(map(int,input().split()))
currentr={0}
for _ in range(K):
    l=list(map(lambda x : int(x)**2,input().split()))[1:]
    nextr=set()
    for num in l:
        for d in currentr:
            nextr.add((d+num)%M)
    currentr=nextr
print(max(currentr))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna