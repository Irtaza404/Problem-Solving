

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(head, data):
    # Write your code here
    
    new_node = DoublyLinkedListNode(data)
    
    # Case 1: empty list
    if head is None:
        return new_node
    
    # Case 2: insert before head
    if data <= head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    
    # Walk to find the right spot
    curr = head
    while curr.next and curr.next.data < data:
        curr = curr.next
    
    # Case 3 & 4: insert after curr (middle or end)
    new_node.next = curr.next
    new_node.prev = curr
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node
    
    return head



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna