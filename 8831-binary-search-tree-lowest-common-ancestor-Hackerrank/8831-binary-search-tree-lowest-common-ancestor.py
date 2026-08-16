

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    #Enter your code here
    if v2<v1:
        v1,v2=v2,v1
    while root!=None:
        if v1<root.info and v2<root.info:
            root=root.left
            
        if v1>root.info and v2>root.info:
            root=root.right
                    
        if v1<=root.info and v2>=root.info:
            return root
            
     
    



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna