class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''Complexity O(N)'''

        prefix = 0 # Stores the prefix of the sum. We 'erase' it if it is negative (i.e. it'll only decrease the sum)
        bigsum = float('-inf') # Store the maximal sum. Starts with - infinity for comparison measures.

        for i in nums: 
            prefix += i # Increments the prefix 
            bigsum = max(bigsum, prefix) # See if it is the new maximal
            prefix = max(prefix, 0) # Erases it if negative

        return bigsum
