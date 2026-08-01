m=int(input())
while(m):
    n=int(input())
    a=input()
    b=dict()
    ans=0
    for i in a:
        if i not in b:
            ans+=2
            b[i]=1
        else:
            ans+=1
            b[i]+=1
    m-=1
    print(ans)
