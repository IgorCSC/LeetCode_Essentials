class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = dict()

        for i in nums:
            if i in table:
                return True
            else: 
                table[i] = 1
        
        return False
