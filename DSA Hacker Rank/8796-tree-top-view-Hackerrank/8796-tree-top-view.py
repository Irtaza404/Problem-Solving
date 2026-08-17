

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque
def topView(root):
    #Write your code here
    if root==None:
        return 
    
    hd_map={}
    q=deque([(root,0)])
    
    while q:
        node,hd=q.popleft()
        if hd not in hd_map:
            hd_map[hd]=node
        
        if node.left:
            q.append((node.left,hd-1))
        if node.right:
            q.append((node.right,hd+1))
        
    
    for i in sorted(hd_map.keys()):
        print(hd_map[i],end=" ")
            
    
    
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna