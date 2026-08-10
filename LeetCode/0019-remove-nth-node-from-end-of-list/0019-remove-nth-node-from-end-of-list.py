# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(0, head)
        l=0
        temp=head
        while temp is not None:
            l+=1
            temp=temp.next
    
        temp = dummy   
        t = 0
        while t != (l - n):  
            t += 1
            temp = temp.next
        temp.next = temp.next.next
        return dummy.next  





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna