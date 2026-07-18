t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))

    for i in n:
        print(min(i, a[0] - 1), end=" ")
    print()
