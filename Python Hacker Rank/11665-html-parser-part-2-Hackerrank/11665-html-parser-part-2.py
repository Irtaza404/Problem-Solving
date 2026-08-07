from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    # Overriding the method for Comments
    def handle_comment(self, data):
        # If there is a newline character in the data, it spans multiple lines
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
        
    # Overriding the method for Data (text content)
    def handle_data(self, data):
        # HTML often has random newlines between tags; we need to ignore those empty lines
        if data != '\n':
            print(">>> Data")
            print(data)

# --- HackerRank's provided stub code ---
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna