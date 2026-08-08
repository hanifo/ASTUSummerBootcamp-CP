t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    freq = {}
    for x in s:
        freq[x] = freq.get(x, 0) + 1

    if 1 in freq.values():
        print(-1)
        continue

    ans = [0] * n
    i = 0

    while i < n:
        j = i

        while j < n and s[j] == s[i]:
            j += 1

        for k in range(i, j - 1):
            ans[k] = k + 2

        ans[j - 1] = i + 1

        i = j

    print(*ans)
