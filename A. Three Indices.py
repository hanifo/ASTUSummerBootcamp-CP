t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    left = [0] * n
    mn = 0

    for i in range(n):
        if p[i] < p[mn]:
            mn = i
        left[i] = mn

    right = [0] * n
    mn = n - 1

    for i in range(n - 1, -1, -1):
        if p[i] < p[mn]:
            mn = i
        right[i] = mn

    found = False

    for j in range(1, n - 1):
        if p[left[j]] < p[j] and p[right[j]] < p[j]:
            print("YES")
            print(left[j] + 1, j + 1, right[j] + 1)
            found = True
            break

    if not found:
        print("NO")
