t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []
    while True:
        done = True
        moved = False
        for x in b:
            if x != k + 1:
                done = False
                break
        if done:
            break
        for i in range(n):
            if b[i] == k + 1:
                continue
            nxt = b[i] + 1
 
            if nxt == k + 1 or b.count(nxt) < a[nxt - 1]:
                b[i] += 1
                ans.append(i + 1)
                moved = True
                break
 
        if not moved:
            ans = [-1]
            break
 
    if ans == [-1]:
        print(-1)
    else:
        print(len(ans))
        if ans:
            print(*ans)
