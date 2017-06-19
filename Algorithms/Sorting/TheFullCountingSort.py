n = int(input().strip())
arr = []
for _ in range(n):
    line = input().strip().split(' ')
    arr.append([int(line[0]), line[1]])
    
for i in range(n//2):
    arr[i][1] = "-"
    
# d is the number of index occurence     
d = {i: 0 for i in range(n)}
for x in arr:
    d[x[0]] += 1
    
# d becomes the number of occurences lower or equal to the index
for i in range(n - 1):
    d[i+1] += d[i]
    
ans = [""] * n
l = 0
for x in arr[::-1]:
    ans[d[x[0]] - 1] = x[1]
    d[x[0]] -= 1
    
print(*ans)
