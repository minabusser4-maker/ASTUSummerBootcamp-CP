t=int(input())
for _ in range(t):
    a=int(input())
    c=list(map(int,input().split()))
    mx=max(c)
    for i in range(a):
        b=c[:]
        b.pop(i)
        print(c[i]-max(b),end=" ")
    print()

            
