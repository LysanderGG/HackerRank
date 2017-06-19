def insertion_sort(l):
    nb_shifts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            nb_shifts += 1
        l[j+1] = key
    return nb_shifts

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
nb_shifts = insertion_sort(ar)
print(nb_shifts)
