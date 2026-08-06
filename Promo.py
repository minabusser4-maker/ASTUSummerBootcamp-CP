n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for _ in range(q):
    x, y = map(int, input().split())
    start = n - x
    print(sum(a[start:start + y]))
