t = int(input())
 
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    nums = list(range(1, n + 1))
    ans = []
    ok = True
 
    for i in range(n):
        found = False
        for x in nums:
            if x != p[i]:
                if len(nums) == 2:
                    other = nums[0] if nums[1] == x else nums[1]
                    if other == p[i + 1]:
                        continue
                ans.append(x)
                nums.remove(x)
                found = True
                break
        if not found:
            ok = False
            break
    if ok:
        print(*ans)
    else:
        print(-1)
