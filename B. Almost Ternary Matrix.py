t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    for i in range(n):
        row=[]
        for j in range(m):
            x=(i+j)%2
            if (i//2+j//2)%2:x=1-x
            row.append(x)
        print(*row)
