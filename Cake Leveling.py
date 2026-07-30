t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    s = 0
    best = 10**18
    for i in range(n):
        s += a[i]
        h = s // (i + 1)
        best = min(best, h)
        ans.append(best)

    print(*ans)
