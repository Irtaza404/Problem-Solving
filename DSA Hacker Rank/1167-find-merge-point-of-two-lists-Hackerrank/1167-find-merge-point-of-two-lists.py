

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    def length(node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n
    len1, len2 = length(head1), length(head2)
    t1, t2 = head1, head2

    if len1 > len2:
        for _ in range(len1 - len2):
            t1 = t1.next
    else:
        for _ in range(len2 - len1):
            t2 = t2.next
    while t1 != t2:
        t1 = t1.next
        t2 = t2.next

    return t1.data
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna