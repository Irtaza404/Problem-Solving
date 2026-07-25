# Enter your code here. Read input from STDIN. Print output to STDOUT
A,B=map(int,input().split())
group1=[]
group2=[]
for i in range(A):
    group1.append(input())
for i in range(B):
    group2.append(input())

for c in group2:
    check = True
    for l in range(0,A):
        if c==group1[l]:
            print(l+1,end=" ")
            check = False
    if check:
        print(-1)
    else:
        print()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna