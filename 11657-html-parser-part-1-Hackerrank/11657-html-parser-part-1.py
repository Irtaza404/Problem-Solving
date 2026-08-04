from html.parser import HTMLParser

# 1. Create a custom subclass of HTMLParser
class MyHTMLParser(HTMLParser):
    
    # Overriding the method for Start Tags
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
            
    # Overriding the method for End Tags
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
        
    # Overriding the method for Empty Tags (like <br /> or <img />)
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == '__main__':
    # 2. Read the number of lines
    n = int(input())
    
    # 3. Read all the HTML code into a single string
    html_code = ""
    for _ in range(n):
        html_code += input()
        
    # 4. Instantiate our custom parser and feed it the HTML
    parser = MyHTMLParser()
    parser.feed(html_code)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna