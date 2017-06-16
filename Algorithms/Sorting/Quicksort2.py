def partition(ar):
    if len(ar) <= 1:
        return ar
    
    left = []
    right = []
    p = ar[0]
    for x in ar:
        if x < p:
            left.append(x)
        elif x > p:
            right.append(x)
    merged = partition(left) + [p] + partition(right)
    print(*merged)
    return merged

            
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
partition(ar)