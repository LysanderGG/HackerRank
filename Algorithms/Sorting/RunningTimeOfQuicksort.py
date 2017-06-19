def insertion_sort(l):
    nb_shifts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            nb_shifts += 1
        l[j+1] = key
    return nb_shifts


def in_place_quicksort(arr, lo, hi):
    if hi <= lo:
        return 0
    
    nb_swaps = 0
    p = arr[hi]
    le = lo - 1 # left end
    for i in range(lo, hi):
        if arr[i] <= p:
            nb_swaps += 1
            le += 1
            if i != le:
                arr[i], arr[le] = arr[le], arr[i]
    arr[hi], arr[le+1] = arr[le+1], arr[hi]
    nb_swaps += 1
    
    nb_swaps += in_place_quicksort(arr, lo, le)
    nb_swaps += in_place_quicksort(arr, le + 2, hi)
    return nb_swaps


n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
arr2 = list(arr)
nb_swaps_qsort = in_place_quicksort(arr, 0, len(arr) - 1)
nb_shifts_insertion = insertion_sort(arr2)
ans = nb_shifts_insertion - nb_swaps_qsort
print(ans)