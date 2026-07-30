# Enter your code here. Read input from STDIN. Print output to STDOUT
x,k=map(int,input().split())
poly=input()
print(eval(poly.replace("x",str(x)))==k)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna