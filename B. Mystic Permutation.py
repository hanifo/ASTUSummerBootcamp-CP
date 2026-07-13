t= int(input())

for _ in range(t):
    n= int(input())
    p= list(map(int, input().split()))

    if n==1:
        print(-1)
        continue

    ans= []
    for i in range(1, n + 1):
        ans.append(i)

    for i in range(n - 1):
        if ans[i]==p[i]:
            ans[i], ans[i + 1]= ans[i + 1], ans[i]

    if ans[n - 1]==p[n - 1]:
        ans[n - 1], ans[n - 2]= ans[n - 2], ans[n - 1]

    print(*ans)
