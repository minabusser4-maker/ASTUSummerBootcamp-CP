from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
    nums = [3, 9, 7]
sol = Solution()
print(sol.minOperations([3,9,7], 5))

