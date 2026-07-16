def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0 and ( not year%100==0 or year%400==0):
        return True
    return leap



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna