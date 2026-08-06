t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    
    if len(set(m)) < n:
        print("YES")
    else:
        print("NO")
