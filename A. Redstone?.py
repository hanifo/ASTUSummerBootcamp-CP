t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ok = False

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                ok = True
                break
        if ok:
            break

    if ok:
        print("YES")
    else:
        print("NO")
