class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        chars_dict = {}
        sub = 0
        act_sub = 0

        for i in range(len(s)):
            char = s[i]
            if char in chars:
                chars = set(s[chars_dict[char]:i])
                act_sub = len(s[chars_dict[char]:i])
                chars_dict[char] = i
            else:
                chars.add(char)
                chars_dict[char] = i
                act_sub += 1
            sub = max(sub, act_sub)
        
        return sub
