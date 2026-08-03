def wrapper(f):
    def fun(l):
        # complete the function
        n=[]
        for i in l:
            match len(i):
                case 13:pass
                case 12:i=f"+{i}"
                case 11:i=f"+91{i[1:]}"
                case 10:i=f"+91{i}"
            n.append(f"{i[0:3]} {i[3:8]} {i[8:]}")
        f(n)
    return fun



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna