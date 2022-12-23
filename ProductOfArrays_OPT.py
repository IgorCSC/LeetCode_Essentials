class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Prefix, Postfix = [1], [1]
        size = len(nums)
        out = []

        for i in range(size-1):
            no_pre = nums[i]
            no_pos = nums[size - 1 - i]

            Prefix.append(Prefix[-1] * no_pre)
            Postfix.insert(0, Postfix[0] * no_pos)

            print(no_pre, no_pos)

        
        print(Prefix, Postfix)

        for i in range(size):
            out.append(Prefix[i]*Postfix[i])
        return out
