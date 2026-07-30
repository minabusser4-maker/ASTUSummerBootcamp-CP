t = int(input())
 
for i in range(t):
    n = int(input())
    s = list(map(int, input().split())) 
    s.sort()
 
    yes = True
 
    for i in range(1, n - 1, 2):
      if s[i] != s[i + 1]:
        yes = False
        break
 
    print("YES" if yes else "NO")
 
    
 
 
