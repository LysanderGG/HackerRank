def in_place_quicksort(arr, lo, hi):
    if hi <= lo:
        return
    
    p = arr[hi]
    le = lo - 1 # left end
    for i in range(lo, hi):
        if arr[i] <= p:
            le += 1
            if i != le:
                arr[i], arr[le] = arr[le], arr[i]
    arr[hi], arr[le+1] = arr[le+1], arr[hi]
    
    print(*arr)
    in_place_quicksort(arr, lo, le)
    in_place_quicksort(arr, le + 2, hi)
    

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
in_place_quicksort(arr, 0, len(arr) - 1)
