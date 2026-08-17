# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true
# Problem     Tree: Huffman Decoding 
# Difficulty  Medium
# Subdomain   Trees
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 12:12 a.m.
# ──────────────────────────────────────────────────



"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    reset=True
    res=""
    for i in s:
        if reset:
            t=root
        while True:
            if i=="0":
                t=t.left
                if t.left is None and t.right is None:
                    res+=t.data
                    reset=True
                    break
                else:
                    reset=False
                    break
            else:
                t=t.right
                if t.left is None and t.right is None:
                    res+=t.data
                    reset=True
                    break
                else:
                    reset=False
                    break
    print(res)
