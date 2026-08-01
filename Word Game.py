t=int(input())
for _ in range(t):
    n=int(input())
    a=input().split()
    b=input().split()
    c=input().split()
    m1=m2=m3=0
    for i in a:
        if i not in b and i not in c:
            m1+=3
        elif i in b and i not in c:
            m1+=1
        elif i in c and i not in b:
            m1+=1
    for i in b:
        if i not in a and i not in c:
            m2+=3
        elif i in a and i not in c:
            m2+=1
        elif i in c and i not in a:
            m2+=1
    for i in c:
        if i not in a and i not in b:
            m3+=3
        elif i in a and i not in b:
            m3+=1
        elif i in b and i not in a:
            m3+=1
    print(m1, m2, m3)
