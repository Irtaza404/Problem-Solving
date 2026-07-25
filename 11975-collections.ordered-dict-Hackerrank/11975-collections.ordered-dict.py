# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
item=OrderedDict()
for _ in range(int(input())):
    word=""
    for i in input().split():
        if i.isalpha():
            word+=f"{i} "
        else:
            digit=int(i)
    
    if word in item.keys():
        item[word]+=digit
    else:
        item[word]=digit
for name ,price in item.items():
    print(f"{name}{price}")
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna