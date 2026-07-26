# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in range(int(input())):
    N=int(input())
    block=deque(map(int,input().split()))
    tower=[]
    check=True
    while block:
        if len(block)==1:
            m=block.pop()
        elif block[0]<block[-1]:
            m=block.pop()
        else:
            m=block.popleft()
        if tower==[]:
            tower.append(m)
        elif tower[-1]>=m:
            tower.append(m)
        else:
            check=False
            break
    
    if check:
        print("Yes")
    else:
        print("No")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna