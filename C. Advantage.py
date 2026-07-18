t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    mx1 = -1
    mx2 = -1

    for i in s:
        if i > mx1:
            mx2, mx1 = mx1, i
        elif i > mx2:
            mx2 = i

    for i in s:
        if i == mx1:
            print(i - mx2, end=" ")
        else:
            print(i - mx1, end=" ")
    print()
