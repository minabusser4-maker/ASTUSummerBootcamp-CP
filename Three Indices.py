t = int(input())
 
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = False
    left_min = p[0]
    left_pos = 0
 
    for j in range(1, n - 1):
        for k in range(j + 1, n):
            if left_min < p[j] and p[k] < p[j]:
                print("YES")
                print(left_pos + 1, j + 1, k + 1)
                ans = True
                break
 
        if ans:
            break
 
        if p[j] < left_min:
            left_min = p[j]
            left_pos = j
 
    if not ans:
        print("NO")
