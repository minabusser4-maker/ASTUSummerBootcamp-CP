t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    pos = []
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            pos.append(i)
    if not pos:
        print("Yes")
    elif pos[-1] - pos[0] + 1 == len(pos):
        print("Yes")
    else:
        print("No")
