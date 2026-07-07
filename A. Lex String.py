t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    a = sorted(input())
    b = sorted(input())

    i = 0
    j = 0

    last = ''
    cnt = 0

    ans = []

    while i < n and j < m:

        if (a[i] < b[j] and not (last == 'a' and cnt == k)) or (last == 'b' and cnt == k):

            ans.append(a[i])
            i += 1

            if last == 'a':
                cnt += 1
            else:
                last = 'a'
                cnt = 1

        else:

            ans.append(b[j])
            j += 1

            if last == 'b':
                cnt += 1
            else:
                last = 'b'
                cnt = 1

    print(''.join(ans))
