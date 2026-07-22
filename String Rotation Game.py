t = int(input())
 
for i in range(t):
    n = int(input())
    s = input()
    ans = 0
 
    for i in range(n):
        m = s[i:] + s[:i]
        cnt = 1
        for j in range(1, n):
            if m[j] != m[j - 1]:
                cnt += 1
        ans = max(ans, cnt) 
    print(ans)
 
 
