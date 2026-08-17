

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        n=Node(val)
        if self.root is None:
            self.root=n
            return self.root
        t=self.root
        while True:
            if val <=t.info:
                if t.left is None:
                   t.left=n
                   return self.root
                else:
                    t=t.left
            else:
                if t.right is None:
                    t.right=n
                    return self.root
                else:
                    t=t.right
        
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna