n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))

d = {i: 0 for i in range(100)}
for x in arr:
    d[x] += 1

print(*[x for (v, n) in d.items() for x in [v]*n])