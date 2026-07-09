t=int(input())

for i in range(t):
    n=int(input())
    s=input()

    a=[]
    for j in range(n//2):
        if s[j]!=s[n-1-j]:
            a.append(j)

    if not a:
        print("Yes")
    elif a[-1]-a[0]+1 == len(a):
        print("Yes")
    else:
        print("No")
