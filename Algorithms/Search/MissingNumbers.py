import collections


n = int(input().strip())
A = collections.Counter(list(map(int, input().strip().split(' '))))
m = int(input().strip())
B = collections.Counter(list(map(int, input().strip().split(' '))))

diff = sorted([*(B - A)])
print(*diff)
