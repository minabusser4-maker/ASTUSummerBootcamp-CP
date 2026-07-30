t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
 
    ans = [[0] * m for _ in range(n)]
 
    for i in range(0, n, 2):
        flag = (i // 2) % 2
 
        for j in range(0, m, 2):
            if flag == 0:
                ans[i][j] = 1
                ans[i][j + 1] = 0
                ans[i + 1][j] = 0
                ans[i + 1][j + 1] = 1
            else:
                ans[i][j] = 0
                ans[i][j + 1] = 1
                ans[i + 1][j] = 1
                ans[i + 1][j + 1] = 0
 
            flag ^= 1
 
    for row in ans:
        print(*row)
