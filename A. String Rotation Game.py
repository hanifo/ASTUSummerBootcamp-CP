t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    res = [s[0]]
    check = False

    for c in s[1:]:
        if c == res[-1]:
            check = True
        else:
            res.append(c)

    print(len(res) + (check and res[0] != res[-1]))
