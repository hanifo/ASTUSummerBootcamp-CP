t = int(input())

for _ in range(t):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    mrg = []

    for i in nums:
        for j in i:
            if j not in mrg:
                mrg.append(j)

    mrg = [k for k in range(1, 2 * n + 1) if k not in mrg] + mrg

    print(*mrg)
