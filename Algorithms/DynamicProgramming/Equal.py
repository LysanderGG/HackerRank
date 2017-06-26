# Note: give one chocolate to everyone but the chosen one
# is the same that removing a chocolate from the chosen one (relatively).
def equilibrate(collegues):
    real_min = min(l)
    nb_ops_l = []
    
    for offset in range(5):
        nb_ops = 0
        m = real_min - offset
        for c in collegues:
            nb_5 = (c - m) // 5
            c -= nb_5 * 5
            nb_ops += nb_5

            nb_2 = (c - m) // 2
            c -= nb_2 * 2
            nb_ops += nb_2

            nb_1 = c - m
            nb_ops += nb_1
        nb_ops_l.append(nb_ops)
        
    return min(nb_ops_l)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    l = [int(_) for _ in input().strip().split(' ')]
    print(equilibrate(l))
