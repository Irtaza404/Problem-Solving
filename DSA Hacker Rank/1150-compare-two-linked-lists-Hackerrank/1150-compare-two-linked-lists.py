

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    while llist1!=None and llist2!=None:
        if llist1.data!=llist2.data:
            return 0
        if llist1.next!=None and llist2.next==None:
            return 0
        elif llist1.next==None and llist2.next!=None:
            return 0
        else:
            llist1=llist1.next
            llist2=llist2.next
        
    return 1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna