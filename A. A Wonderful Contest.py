t=int(input())
for i in range(t):
    n, a = int(input()), list(map(int, input().split()))
    print("YES" if 100 in a else "NO")
