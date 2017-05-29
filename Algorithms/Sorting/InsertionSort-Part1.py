size = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

val = arr[size - 1]
i = size - 2    
while i >= 0 and val < arr[i]:
    arr[i + 1] = arr[i]    
    i -= 1
    print(*arr)
    
arr[i+1] = val
print(*arr)
