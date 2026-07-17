t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    freq = {}

    for i in nums:
        freq[i] = freq.get(i, 0) + 1

    ans = sorted(set(nums))

    for j in set(nums):
        for _ in range(freq[j] - 1):
            ans.append(j)

    print(*ans)
