class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse=0
        temp=x
        while temp!=0:
            n=temp%10
            temp//=10
            reverse=reverse*10+n
        if x==reverse:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna