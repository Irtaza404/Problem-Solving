def merge_the_tools(string, k):
    # your code goes here
    s=len(string)//k
    data=[]
    for i in range(0,len(string),k):
        word=string[i:i+k]
        newword=""
        for w in word:
            if w not in newword:
                newword+=w
        data.append(newword)
    for d in data:
        print(d)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna