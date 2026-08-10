class Solution:
    def myAtoi(self, s: str) -> int:
        
        s=s.strip()
        if not s:
            return 0
        if not (s[0] in ["+","-"] or s[0].isdigit()):
            return 0
        sign="-" if s[0]=="-" else "+"
        num=0
        start=1 if s[0] in ["+","-"] else 0
        for i in range(start,len(s)):
            if not s[i].isdigit() or s[i] in ["+","-"] :
                break
            num = num * 10 + int(s[i])
        if num==0:
            return 0
        else:
            num=-num if sign=="-" else num
        mx,mn=2**31-1,-2**31
        if num > mx:
            return mx
        if num < mn:
            return mn
        return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna