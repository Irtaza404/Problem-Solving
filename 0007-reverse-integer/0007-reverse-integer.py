class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX,INT_MIN=2**31,-2**31-1
        num=0
        temp=x
        x= -x if temp<0 else x
        while x!=0:
            last=x%10 
            x//=10 
            num=num*10+last 
        num=-num if temp<0 else num
        if num > INT_MAX or num < INT_MIN:
            return 0
        return num


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna