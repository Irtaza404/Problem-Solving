import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(rf"{p}",s) is not None:
            return True
        else:return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna