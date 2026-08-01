from collections import Counter
t=int(input())
for _ in range(t):
    a=int(input())
    b=list(map(int,input().split()))
    cnt=Counter(b)
    ans=[]
    for i in sorted(cnt):
        ans.append(i)
        cnt[i]-=1
    for i in sorted(cnt):
        while cnt[i]>0:
            ans.append(i)
            cnt[i]-=1
    print(*ans)
