class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first, *r = sorted(strs, key=len)
        res = ""
        for c in first:
            avl = True
            for word in r:
                if word.startswith(res + c):
                    continue
                else:
                    avl = False
                    break
            if avl:
                res += c
            else:
                break

        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna