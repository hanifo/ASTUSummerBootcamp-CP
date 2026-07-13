t= int(input())

for _ in range(t):
    n, q= map(int, input().split())
    a= list(map(int, input().split()))

    prefix= [0]* (n + 1)
    for i in range(n):
        prefix[i + 1]= prefix[i] + a[i]

    total= prefix[n]

    for _ in range(q):
        l, r, k= map(int, input().split())

        old= prefix[r] - prefix[l - 1]
        new_sum= total - old + (r - l + 1) * k

        if new_sum % 2== 1:
            print("YES")
        else:
            print("NO")
