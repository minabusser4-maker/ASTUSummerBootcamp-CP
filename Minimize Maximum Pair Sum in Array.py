class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        for i in range(len(nums)//2):
            small = nums[i]
            large = nums[len(nums)-1-i]

            mx = max(mx, small + large)
        return mx



        
