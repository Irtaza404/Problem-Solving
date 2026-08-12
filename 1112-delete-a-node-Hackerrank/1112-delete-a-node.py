

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # Write your code here
    if llist==None:
        return llist
    count=0
    temp=llist
    while temp!=None:
        count+=1
        temp= temp.next
    temp=llist
    i=0
    if position==0:
        llist=llist.next
        return llist
    while i<position-1 and i<count:
        i+=1
        temp=temp.next
    temp.next=temp.next.next
    
    return llist


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna