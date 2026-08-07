from html.parser import HTMLParser

# Create a custom subclass of HTMLParser
class MyHTMLParser(HTMLParser):
    
    # Method for standard start tags (like <div> or <a href="...">)
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
            
    # Method for empty tags (like <img src="..."> or <br/>)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == '__main__':
    # Read the number of lines
    n = int(input())
    
    # Read all the HTML code into a single string
    html_code = ""
    for _ in range(n):
        html_code += input()
        
    # Instantiate our custom parser and feed it the HTML
    parser = MyHTMLParser()
    parser.feed(html_code)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna