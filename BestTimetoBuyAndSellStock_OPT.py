class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Code idea by Neet Code'''

        ind1, ind2 = 0, 1
        diff = 0

        while ind2 < len(prices):
            buy = prices[ind1]
            sell = prices[ind2]

            if buy > sell: # move buy to sell
                ind1 = ind2 
                ind2 += 1
            else:
                if diff < sell - buy:
                    diff = sell - buy 
                ind2 += 1
        
        return diff
