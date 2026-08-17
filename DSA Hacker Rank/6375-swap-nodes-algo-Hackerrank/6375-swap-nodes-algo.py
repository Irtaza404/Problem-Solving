#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000)
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_tree(indexes):
    n = len(indexes)
    nodes = [Node(i + 1) for i in range(n)]  # values are 1-indexed node numbers
    
    for i in range(n):
        left, right = indexes[i]
        if left != -1:
            nodes[i].left = nodes[left - 1]
        if right != -1:
            nodes[i].right = nodes[right - 1]
    
    return nodes[0]  # root

def swap_at_depths(node, depth, k):
    if node is None:
        return
    if depth % k == 0:
        node.left, node.right = node.right, node.left
    swap_at_depths(node.left, depth + 1, k)
    swap_at_depths(node.right, depth + 1, k)

def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)

def swapNodes(indexes, queries):
    root = build_tree(indexes)
    answers = []
    
    for k in queries:
        swap_at_depths(root, 1, k)   # depth starts at 1 for root
        result = []
        inorder(root, result)
        answers.append(result)
    
    return answers
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna