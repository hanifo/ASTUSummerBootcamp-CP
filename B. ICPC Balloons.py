t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    check = set()
    check.add(s[0])
    res = 1
    
    for i in s:
        if i in check:
            res += 1
        else:
            res += 2
            check.add(i)
    
    print(res)
