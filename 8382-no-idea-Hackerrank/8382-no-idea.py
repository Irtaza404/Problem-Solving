# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
array=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
happiness=0
for num in array:
    if num in a:
        happiness+=1
    if num in b:
        happiness-=1
    
print(happiness)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna