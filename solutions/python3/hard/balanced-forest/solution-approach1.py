# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/balanced-forest/problem?isFullScreen=true
# Problem     Balanced Forest
# Difficulty  Hard
# Subdomain   Trees
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-18, 09:19 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re


#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

import sys

# Increase recursion depth just in case the tree is a deep line
sys.setrecursionlimit(100000)

def balancedForest(c, edges):
    n = len(c)
    
    # 1. Build Adjacency List
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # 2. First DFS to compute sum of subtrees
    subtree_sum = [0] * (n + 1)
    
    def dfs1(u, p):
        s = c[u - 1]
        for v in adj[u]:
            if v != p:
                s += dfs1(v, u)
        subtree_sum[u] = s
        return s
        
    dfs1(1, 0)
    T = subtree_sum[1]
    
    # Global minimum weight W
    min_w = float('inf')
    
    # Track the sums we have seen so far
    visited_sums = set()
    path_sums = set()
    
    # 3. Second DFS to find the cuts
    def dfs2(u, p):
        nonlocal min_w
        C = subtree_sum[u]
        
        # Option A: C acts as the target component sum S
        S = C
        if 3 * S >= T:
            # Check if we can find the required matching cuts
            if (S in visited_sums or 
                (T - 2 * S) in visited_sums or 
                (2 * S) in path_sums or 
                (T - S) in path_sums):
                min_w = min(min_w, 3 * S - T)
                
        # Option B: C acts as the smaller leftover component (T - 2S)
        if (T - C) % 2 == 0:
            S2 = (T - C) // 2
            if 3 * S2 >= T:
                # Check if we can find the required matching cuts
                if (S2 in visited_sums or 
                    (S2 + C) in path_sums):
                    min_w = min(min_w, 3 * S2 - T)
                    
        # Before visiting children, add current node's sum to path
        path_sums.add(C)
        
        # Traverse children
        for v in adj[u]:
            if v != p:
                dfs2(v, u)
                
        # After visiting all children, remove from path and add to fully visited
        path_sums.remove(C)
        visited_sums.add(C)

    dfs2(1, 0)
    
    return min_w if min_w != float('inf') else -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
