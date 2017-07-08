t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    n = ~n & 0xffffffff
    print(n)