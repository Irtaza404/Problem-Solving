

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

#
#

def getNode(llist, positionFromTail):
    # Write your code here
    fast=llist
    for _ in range(positionFromTail+1):
        if fast:
            fast=fast.next
    slow=llist
    while fast!=None:
        fast=fast.next
        slow=slow.next
    return slow.data


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna