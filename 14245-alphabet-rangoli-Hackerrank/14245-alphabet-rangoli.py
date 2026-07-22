def print_rangoli(size):
    # your code goes here
    col = 4 * size - 3
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    for i in range(size - 1, -1, -1):
        text = "-".join(alphabet[i:size][::-1])
        text = f"{text}{text[::-1][1:]}"
        # print(text)
        lst.append(text.center(col, "-"))
    
    lst.extend(lst[:-1][::-1])
    for l in lst:
        print(l)
    return "\n".join(lst)
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna