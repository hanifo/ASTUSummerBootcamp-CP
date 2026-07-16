t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    good = {nums[-1]}  
    for i in nums[-2::-1]: 
        if i in good:
            break
        else:
            good.add(i)
    
    print(n - len(good))  
