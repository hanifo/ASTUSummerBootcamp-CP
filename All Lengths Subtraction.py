t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    check = True
    
    for k in range(1, n + 1):
        maximum = -1
        start = 0
        
        for i in range(n - k + 1):
            current = 0
            for j in range(i, i + k):
                current += p[j]
            if current > maximum:
                maximum = current
                start = i
        
        for j in range(start, start + k):
            p[j] -= 1
        
        for num in p:
            if num < 0:
                check = False
                break
        
        if not check:
            break
    
    if check:
        for num in p:
            if num != 0:
                check = False
                break
    
    print("YES" if check else "NO")
