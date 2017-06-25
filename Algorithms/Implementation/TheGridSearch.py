#!/bin/python3
import sys

# return True if G contains P
def contains(G, P):
    first_line = P[0]
    sub_len = len(first_line)
    for g_idx in range(len(G) - len(P) + 1):
        try:
            start_idx = 0
            row = G[g_idx]
            while(1):
                idx = row.index(first_line, start_idx)
                start_idx = idx+1
                if len(P) == 1 or all(lineG[idx:idx+sub_len] == lineP for lineP, lineG in zip(P[1:], G[g_idx+1:])):
                    return True
            
        except ValueError:
            pass
    return False

        
t = int(input().strip())
for _ in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for _ in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for _ in range(r):
        P_t = str(input().strip())
        P.append(P_t)
        
    ans = contains(G, P)
    print("YES" if ans else "NO")
