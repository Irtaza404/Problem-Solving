# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
middle=n//2
text=".|."
for i in range(middle):
    print((text*(i*2+1)).center(m, "-"))
print("WELCOME".center(m,"-"))
for i in range(middle,0,-1):
    print((text*(i*2-1)).center(m, "-"))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna