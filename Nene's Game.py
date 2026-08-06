t = int(input())
 
for _ in range(t):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = a[0] - 1
    ans = []
    for i in b:
        ans.append(str(min(i, x)))
    print(*ans)
