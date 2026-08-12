

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            return 1
    return 0    
    # if head==None:
    #     return 0
    # s=set()
    # temp=head
    # while temp and temp.next:
    #     if temp in s:
    #         return 1
    #     s.add(temp)
    #     temp=temp.next
    # return 0



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna