def swap_case(s):
    ch=""
    for c in s:
        c=ord(c)
        if 65<=c<=90:
            ch+=chr(c+32)
        elif 97<=c<=122:
            ch+=chr(c-32)
        else:
            ch+=chr(c)
    return ch



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna