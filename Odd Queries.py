t = int(input())
 
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
 
    for i in range(n):
        prefix[i + 1] = prefix[i] + (a[i] % 2)
    total_odd = prefix[n]  
 
    for _ in range(q):
        l, r, k = map(int, input().split())
        odd_in_range = prefix[r] - prefix[l - 1]
        length = r - l + 1
        new_odd = total_odd - odd_in_range
        if k % 2 == 1:
            new_odd += length
        if new_odd % 2 == 1:
            print("YES")
        else:
            print("NO")
