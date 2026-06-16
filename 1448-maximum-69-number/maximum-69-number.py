class Solution:
    def maximum69Number (self, num: int) -> int:
        s= list(str(num))
        for ch in range(len(s)):
            if s[ch] == '6':
                s[ch] = '9'
                break
        return int("".join(s))        