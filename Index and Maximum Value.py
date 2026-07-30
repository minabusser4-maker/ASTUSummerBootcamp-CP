t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
 
    for _ in range(m):
        c, l, r = input().split()
        l = int(l)
        r = int(r)
 
        for i in range(n):
            if l <= a[i] <= r:
                if c == '+':
                    a[i] += 1
                else:
                    a[i] -= 1
 
        ans.append(str(max(a)))
 
    print(" ".join(ans))
