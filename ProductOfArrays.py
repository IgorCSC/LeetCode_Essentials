class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        C = []
        Prod = 1
        Zero = 0
        for i in nums:
            if i != 0:
                Prod = Prod * i
            else:
                Zero += 1

        for i in nums:
            if Zero > 1 or (i != 0 and Zero > 0):
                C.append(0)
            elif i == 0:
                C.append(int(Prod))
            else:
                C.append(int(Prod/i))

        return C
