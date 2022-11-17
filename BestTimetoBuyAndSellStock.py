class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ma = prices[-1]
        diff = 0 
        
        for i in range(len(prices)):
            no = prices[-i-1]
            ma = max(ma, no)
            if diff < ma - no:
                diff = ma - no 
        
        return diff
