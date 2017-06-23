#return the pair of indexes in prices that sums to m
def solve(prices, m):
    for i in range(len(prices) - 1):
        complement = m - prices[i]
        if complement > 0:
            try:
                complement_idx = i + 1 + prices[i+1:].index(complement)
                return i, complement_idx
            except ValueError:
                pass
                
    # Should not append according to the problem statement.
    return None
            
    

t = int(input().strip())
for _ in range(t):
    m = int(input().strip())
    n = int(input().strip())
    prices = list(map(int, input().strip().split(' ')))
    ans = solve(prices, m)
    print(ans[0]+1, ans[1]+1)