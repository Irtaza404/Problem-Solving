class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_area=0
        while l!=r:
            width = r - l
            h = min(height[l], height[r])
            area = width * h
            max_area=max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna