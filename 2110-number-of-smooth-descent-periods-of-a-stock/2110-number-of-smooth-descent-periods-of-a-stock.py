class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        streak = 0
        for i in range(len(prices)):
            if prices[i] == prices[i-1] -1:
                streak += 1
            else:
                streak = 1
            res += streak 
        return res
        
        