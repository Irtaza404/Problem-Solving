
def person_lister(f):
    def inner(people):
        # complete the function
        ppeo=[]
        for p in sorted(people,key=lambda x:int(x[2])):
            ppeo.append(f(p))
        return ppeo
    return inner



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna