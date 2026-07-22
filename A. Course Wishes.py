t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = []

    for i in range(k,0,-1):
        for j in range(n):
            if b[j]==i:
                while b[j] < k + 1:
                    ans.append(j + 1)
                    b[j] += 1

    print(len(ans))
    if ans:
        print(*ans)
    else:
        print()
