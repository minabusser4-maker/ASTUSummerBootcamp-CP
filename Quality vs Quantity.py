t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    blue_sum = a[0] + a[1]
    red_sum = a[-1]
    i = 2          
    j = n - 2       
    if red_sum > blue_sum:
        print("YES")
        continue
    possible = False
    while i < j:
        blue_sum += a[i]
        red_sum += a[j]
        if red_sum > blue_sum:
            possible = True
            break
        i += 1
        j -= 1
 
    print("YES" if possible else "NO")    
