import re

for _ in range(int(input())):
    card = input().strip()
    
    # Step 1: Check the structure (starts with 4,5,6 -> 16 continuous OR 4 groups of 4 separated by hyphens)
    if re.match(r"^[456]([\d]{15}|[\d]{3}-[\d]{4}-[\d]{4}-[\d]{4})$", card):
        
        # Step 2: Strip the hyphens so we can easily check for consecutive digits
        card_no_hyphens = card.replace("-", "")
        
        # Check for 4 or more consecutive repeating characters
        if re.search(r"(\d)\1{3}", card_no_hyphens):
            print("Invalid")
        else:
            print("Valid")
            
    else:
        print("Invalid")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna