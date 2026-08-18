class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float('inf')
        for window_size in range(l, r + 1):
            window_sum = sum(nums[:window_size])
            if window_sum > 0:
                result = min(result, window_sum)
            for i in range(window_size, len(nums)):
                window_sum += nums[i]
                window_sum -= nums[i - window_size]
                if window_sum > 0:
                    result = min(result, window_sum)
        return -1 if result == float('inf') else result
        