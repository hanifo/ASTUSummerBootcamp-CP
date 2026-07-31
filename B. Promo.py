n, q = map(int, input().split())

p = list(map(int, input().split()))
p.sort(reverse=True)

prefix = [0]
for i in p:
    prefix.append(prefix[-1] + i)

for _ in range(q):
    x, y = map(int, input().split())
    print(prefix[x] - prefix[x-y])
