t = int(input())
 
for i in range(t):
    n = int(input())
    s = input()
 
    ans=0
    for _ in range (len(s)):
        if s[_]!=s[-1]:
            ans += 1
    print(ans)
 
