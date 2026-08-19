# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/balanced-forest/problem?isFullScreen=true
# Problem     Balanced Forest
# Difficulty  Hard
# Subdomain   Trees
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 03:30 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(100000)
#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

def balancedForest(c, edges):
    # Write your code here
    n= len(c)
    adj=[[] for _ in range(n+1)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    subtrees=[0]*(n+1)
    
    def dfs1(u,p):
        s=c[u-1]
        for v in adj[u]:
            if v!=p:
                s+=dfs1(v,u)
        subtrees[u]=s
        return s
    
    dfs1(1,0)
        
    T=subtrees[1]
    minw=float("inf")
    visited=set()
    path=set()
    
    def dfs2(u,p):
        nonlocal minw
        C=subtrees[u]
        if 3*C>=T:
            if (C in visited or (T-2*C) in visited or (2*C) in path or (T-C) in path):
                minw=min(minw,3*C-T)
        if (T-C)%2==0:
            s2=(T-C)//2
            if 3*s2>=T:
                if (s2 in visited or (s2+C) in path):
                    minw=min(minw,3*s2-T)
        
        path.add(C)
        
        for v in adj[u]:
            if v!=p:
                dfs2(v,u)
        path.remove(C)
        visited.add(C)
        
    dfs2(1,0)
        
    return minw if minw!=float("inf") else -1    
        
        
        
        
        
        
        
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
