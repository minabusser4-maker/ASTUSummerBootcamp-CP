for i in range(int(input())):
 
    n=int(input())
    m=list(map(int,input().split()))
    
    maxi=max(m)
    mini=min(m)
    count=(maxi-mini+1)//2
 
    print(count)
