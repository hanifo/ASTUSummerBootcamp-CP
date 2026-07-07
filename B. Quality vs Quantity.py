t=int(input())
for i in range(t):
    n, a= int(input()), list(map(int, input().split()))
    a.sort()
    blue_sum, red_sum=a[0], 0
    left, right=1, n-1
    check=False
    while left<=right:
        if blue_sum+a[left]<red_sum+a[right]:
            check=True
            break
        else:
            blue_sum+=a[left]
            red_sum+=a[right]
            left+=1
            right-=1
    print('YES' if check else 'NO')
