t=int(input())
for i in range(t):
    n, s=int(input()), input()
    print(n-s.count(s[len(s)-1]))
