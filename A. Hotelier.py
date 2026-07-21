n = int(input())
s = input()
res = [0] * 10

for i in range(n):
    if s[i] == 'L':
        p = 0
        while res[p] != 0: p += 1
        res[p] = 1
    elif s[i] == 'R':
        p = -1
        while res[p] != 0: p -= 1
        res[p] = 1
    else:
        res[int(s[i])] = 0

print(''.join(map(str, res)))
