class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        max_len=0
        for i,b in enumerate(s):
            if b=="(":
                stack.append(i)
            else:
                stack.pop()
                if stack==[]:
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna