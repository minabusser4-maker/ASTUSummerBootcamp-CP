t = int(input())
for _ in range(t):
    n, m= map(int, input().split())
    a = list(map(int, input().split()))
    ans = [-1] * (n + 1)
    view = set()
    cur = n 
    for i in range(m):
        if a[i]  not in view:
            view.add(a[i])
            if cur >= 1:
                ans[cur] = i + 1
                cur -= 1
    print(*ans[1:])
