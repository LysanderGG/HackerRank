size = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

for i in range(1, size):
    val = arr[i]
    j = i - 1    
    while j >= 0 and val < arr[j]:
        arr[j + 1] = arr[j]    
        j -= 1
    arr[j+1] = val
    print(*arr)
