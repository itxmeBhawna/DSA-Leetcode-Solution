class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1,-1,-1]
        count = 0
        for i in range(len(s)):
            last[ord(s[i])- ord('a')] = i 
            count += min(last) +1
        return count    



        