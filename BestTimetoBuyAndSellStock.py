class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        biggest = [0]

        '''record max for each section of the list'''
        for i in prices[::-1]:
            last_no = biggest[0]
            if i > last_no:
                biggest.insert(0,i)
            else:
                biggest.insert(0,last_no)
        biggest.pop()

        '''find the difference for each buying point''' 
        diff = 0 
        i = 0

        while i+1 < len(prices):
            no1 = prices[i]
            if diff < biggest[i+1] - no1:
                diff = biggest[i+1] - no1
            i += 1
        
        return diff

