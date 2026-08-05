t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pre1 , pre2 = [0] * n, [0] * n

    s1 , s2 = 0, 0

    for i in range(n):
        if a[i] == 1:
            s1 , s2 = s1 + 1, s2 + 1
        elif a[i] == 2:
            s1, s2 = s1 - 1, s2 + 1
        else:
            s1, s2 = s1 - 1, s2 - 1

        pre1[i], pre2[i] = s1, s2

    best = float('inf')
    check = False

    for j in range(1, n - 1):
        i = j - 1

        if pre1[i] >= 0:
            best = min(best, pre2[i])

        if best <= pre2[j]:
            check = True
            break

    print("YES" if check else "NO")
