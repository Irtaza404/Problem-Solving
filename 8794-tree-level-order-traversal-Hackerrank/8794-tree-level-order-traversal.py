

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque 
def levelOrder(root):
    #Write your code here
    if root is None:
        return
    lvlor=[]
    q=deque([root])
    while q:
        node=q.popleft()
        lvlor.append(node.info)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    for i in lvlor:
        print(i,end=" ")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna