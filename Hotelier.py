t=int(input())
n=input()
rooms=[0]*10
for i in n:
    if i == "L":
        for j in range(10):
            if rooms[j] == 0:
                rooms[j] = 1
                break 
    elif i == "R":
        for j in range(9, -1, -1):
            if rooms[j] == 0:
                rooms[j] = 1
                break
    else:
        rooms[int(i)] = 0
print("".join(map(str, rooms)))
