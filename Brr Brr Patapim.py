t = int(input())
for _ in range(t):
    n = int(input())
    m = [0] * (2 * n + 1)
    used = [False] * (2 * n + 1)
    for i in range (n):
        row = list(map(int, input().split()))
        for j in range(n):
            m[i + j + 2] = row[j]
            used[row[j]] = True
    for i in range(1, 2 * n + 1):
        if not used[i]:
            m[1] = i 
            break
    print(*m[1:])
