def divide(ar, p):
    left = []
    right = []
    for x in ar:
        if x < p:
            left.append(x)
        elif x > p:
            right.append(x)
    return left + [p] + right


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
ans = divide(ar, ar[0])
print(*ans)