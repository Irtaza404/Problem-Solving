
def minion_game(string):
    s = string
    Stuart = Kevin = 0
    length=len(s)
    for i in range(length):
        if s[i] in "AEIOU":
            Kevin += length-i
        else:
            Stuart += length-i
    print(f"Stuart {Stuart}" if Stuart>Kevin else  f"Kevin {Kevin}"  if Kevin>Stuart else "Draw")
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna