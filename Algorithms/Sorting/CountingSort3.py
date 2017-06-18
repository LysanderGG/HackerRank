n = int(input().strip())
arr = []
for _ in range(n):
    line = input().strip().split(' ')
    arr.append([int(line[0]), line[1]])

d = {i: 0 for i in range(100)}
for x in arr:
    d[x[0]] += 1
    
ans = []    
l = 0
for i in range(100):
    l += d[i]
    ans.append(l)
    
print(*ans)
