

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if  llist==None:
        llist=SinglyLinkedListNode(data)
        return llist
    count=0
    temp=llist
    while temp!=None:
        count+=1
        temp=temp.next
    i=0
    temp=llist
    while i!=position-1 and i<count:
        temp=temp.next
        i+=1
    Node=SinglyLinkedListNode(data)
    Node.next=temp.next
    temp.next=Node
    return llist    
    
    



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna