q = int(input().strip())
for _ in range(q):
    n, k = list(map(int, input().strip().split(' ')))
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    
    A.sort()
    B.sort(reverse=True)
    
    ans = all(a + b >= k for a, b in zip(A, B))
    print("YES" if ans else "NO")