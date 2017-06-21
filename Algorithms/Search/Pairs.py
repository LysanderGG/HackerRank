def pairs(a, k):
    return sum(x - k in a for x in a)


if __name__ == '__main__':
    n, k = list(map(int, input().strip().split(' ')))
    a = set(map(int,  input().strip().split(' ')))
    print(pairs(a, k))
