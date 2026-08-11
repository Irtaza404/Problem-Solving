class Solution:
    def isValid(self, ss: str) -> bool:
        stack=[]
        for s in ss:
            if stack==[] or s =="{" or s=="[" or s=="(":
                stack.append(s)
            elif (stack[-1]=="(" and s==")") or (stack[-1]=="{" and s=="}") or(stack[-1]=="[" and s=="]")  :
                stack.pop()
            else:
                return False
        return False if stack else True 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna