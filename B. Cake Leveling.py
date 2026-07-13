t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    mn = float('inf')

    for i in range(n):
        s += a[i]
        avg = s // (i + 1)
        if avg < mn:
            mn = avg
        print(mn, end=" ")
    print()
