t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split())) 
    a.sort()
    ok = True
    for j in range(1, n - 1, 2):
        if a[j] != a[j + 1]:
            ok = False
            break
    print("YES" if ok else "NO")
