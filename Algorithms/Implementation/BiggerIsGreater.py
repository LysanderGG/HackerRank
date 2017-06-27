# Get the smaller letter in dic strictly bigger than the letter c
def get_bigger_letter(c, dic):
    bigger = None
    for l in dic:
        if l > c:
            if bigger is None:
                bigger = l
            else:
                bigger = min(bigger, l)
    return bigger


def solve(w):
    letters = {}
    for i in range(len(w) - 1, -1, -1):
        c = w[i]
        letters[c] = letters.get(c, 0) + 1
        bigger = get_bigger_letter(c, letters)
        if bigger:
            s = w[0:i] + bigger
            letters[bigger] -= 1
            for letter, count in sorted(letters.items()):
                s += letter[0] * count
            return s
            
    return None

t = int(input().strip())
for _ in range(t):
    w = input().strip()
    ans = solve(w)
    print("no answer" if ans is None else ans)