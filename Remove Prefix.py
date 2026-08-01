t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    visit=set()
    ans=0
    for i in range(n - 1, -1, -1):
        if a[i] in visit:
            ans = i + 1
            break
        visit.add(a[i])
    print(ans)
