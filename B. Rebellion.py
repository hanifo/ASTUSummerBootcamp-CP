t = int(input())
 
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
 
    zeros = s.count(0)
    flag = s[:zeros].count(1)
 
    print(flag)
