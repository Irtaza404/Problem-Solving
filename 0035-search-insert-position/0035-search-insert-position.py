class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid 
            
            if nums[mid]<target:
                lo=mid+1
            else:
                hi=mid-1

        return lo 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna