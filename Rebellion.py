t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = sum(a[:n - s]) 
    print(ans)
