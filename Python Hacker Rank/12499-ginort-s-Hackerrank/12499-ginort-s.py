# Enter your code here. Read input from STDIN. Print output to STDOUT
even = odd = lowercase = uppercase = ""
for i in input():
    if i.isalpha():
        if i.islower():
            lowercase+=i
        else:
            uppercase+=i
    elif i.isdigit():
          if int(i)%2==0:
            even+=i
          else:
            odd+=i
l=[lowercase,uppercase,odd,even]
for i in l:
    print("".join(sorted(i)),end="")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna