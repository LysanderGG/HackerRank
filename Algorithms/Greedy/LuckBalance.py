n, k = list(map(int, input().strip().split(' ')))
important = []
not_important = []
for _ in range(n):
    contest, importance = list(map(int, input().strip().split(' ')))
    if importance == 1:
        important.append(contest)
    else:
        not_important.append(contest)
        
important.sort(reverse=True)
ans = sum(not_important) + sum(important[:k]) - sum(important[k:])
    
print(ans)
