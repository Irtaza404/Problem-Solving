

def get_attr_number(node):
    # your code goes here
    count = len(node.attrib)
    # Recursively add the number of attributes for all child nodes
    for child in node:
        count += get_attr_number(child)
        
    return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna