def is_valid(d):
    return all(i <= n // 4 for i in d.values())


def solve(s, n):
    d = { 'A': 0, 'T': 0, 'C': 0, 'G': 0 }

    min_substr_len = n
    # left limit
    for l in range(n):
        d[s[l]] += 1
        if not is_valid(d):
            d[s[l]] -= 1
            l -= 1
            break

    #print("1. l = ", l)

    # right limit
    for r in range(n - 1, 0, -1):
        d[s[r]] += 1
        if not is_valid(d):
            d[s[r]] -= 1
            r += 1
            break
    
    #print("2. r = ", r)

    min_substr_len = max(0, r - l - 1)

    #print("3. min_substr_len = ", min_substr_len)

    while r > l and l >= 0:
        #print("4. ", l, r)
        d[s[l]] -= 1
        l -= 1
        
        while r >= 0:
            #print("5. ", l, r)
            r -= 1
            d[s[r]] += 1
            if not is_valid(d):
                #print("not valid ", l, r)
                d[s[r]] -= 1
                r += 1
                break

        min_substr_len = min(min_substr_len, max(0, r - l - 1))
        #print("min_substr_len = ", min_substr_len)

    return min_substr_len


n = int(input().strip())
s = input().strip()

ans = solve(s, n)
print(ans)
