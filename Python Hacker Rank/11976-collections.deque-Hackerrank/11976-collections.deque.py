# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    i=input().split()
    match i[0]:
        case "append":d.append(int(i[1]))
        case "pop":d.pop()
        case "popleft":d.popleft()
        case "appendleft":d.appendleft(int(i[1]))

for num in d:
    print(num,end=" ")

 
 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna