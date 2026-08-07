# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for _ in range(n):
    try: 
        a,b=list(map(int,input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print(f"Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna