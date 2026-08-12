

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#'
import heapq
def mergeLists(head1, head2):
    heap=[]
    heapq.heappush(heap,(head1.data,0,head1))
    heapq.heappush(heap,(head2.data,1,head2))
    dummy=SinglyLinkedListNode(0)
    temp=dummy
    while heap:
        val,i,node=heapq.heappop(heap)
        temp.next=node
        temp=temp.next
        if node.next:
            heapq.heappush(heap,(node.next.data,i,node.next))
    return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna