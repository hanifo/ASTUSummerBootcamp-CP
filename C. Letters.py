n, m = map(int, input().split())

a, b = list(map(int, input().split())), list(map(int, input().split()))

prefix , s = [], 0

for x in a:
    s += x
    prefix.append(s)

for room in b:
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if prefix[mid] >= room:
            right = mid - 1
        else:
            left = mid + 1

    dorm = left

    print (*(1, room) if dorm == 0 else (dorm + 1, room - prefix[dorm - 1]))
