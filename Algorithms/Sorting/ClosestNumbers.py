n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

ans = []
m = abs(a[0]-a[1]) # n >= 2, so no problem
a.sort()
for i in range(n-1):
    diff = abs(a[i] - a[i+1])
    if diff <= m:
        if diff < m:
            ans = []
            m = diff
        ans += a[i:i+2]

print(*ans)