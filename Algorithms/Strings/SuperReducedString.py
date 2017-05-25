s = str(input())
do_continue = True

while do_continue:
    do_continue = False
    i = 0
    s_reduced = ""
    
    while i < len(s):
        if i == len(s) - 1:
            s_reduced += s[i]
            break
        else:
            a, b = s[i], s[i+1]
            if a != b:
                s_reduced += a
                i += 1
            else:
                do_continue = True
                i += 2
    s = s_reduced
            
if len(s) > 0:
    print(s)
else:
    print("Empty String")