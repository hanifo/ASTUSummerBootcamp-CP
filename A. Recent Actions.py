t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    ans = [-1] * (n + 1)

    seen = [False] * (n + m + 2)

    cnt = 0
    for i in range(m):
        if not seen[p[i]]:
            seen[p[i]] = True
            cnt += 1
            if cnt <= n:
                ans[n - cnt + 1] = i + 1

    for i in range(1, n + 1):
        print(ans[i], end=" ")
    print()
