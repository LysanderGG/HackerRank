n, k = list(input().strip().split(' '))
k = int(k)

sum_n = str(sum(int(c) for c in n))
sum_n *= k

while(len(sum_n) > 1):
    sum_n = str(sum(int(c) for c in sum_n))
    
print(sum_n)