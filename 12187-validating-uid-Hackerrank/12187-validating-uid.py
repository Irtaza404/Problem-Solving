for _ in range(int(input())):
    uid = input().strip()
    
    # Check all 5 conditions
    if (len(uid) == 10 and 
        uid.isalnum() and 
        len(set(uid)) == 10 and 
        sum(char.isupper() for char in uid) >= 2 and 
        sum(char.isdigit() for char in uid) >= 3):
        
        print("Valid")
    else:
        print("Invalid")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna