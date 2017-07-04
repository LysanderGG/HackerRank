# n XOR n == 0
# 0 XOR n == n
# if N is even digits longs, digits at odd positions are xored an even number of times
# if N is odd digits longs, all digits are xored an odd number of times
def xor(s):
    if len(s) & 1 == 0:
        return 0
    
    ans = 0
    for i in range(len(s)):
        if i & 1 == 0:
            ans ^= s[i]
    return ans

    
t = int(input().strip())
for _ in range(t):
    input()
    s = list(map(int, input().strip().split(' ')))
    print(xor(s))