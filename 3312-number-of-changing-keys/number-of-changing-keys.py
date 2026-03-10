class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        s=s.lower()
        for ch in range(1,len(s)):
            if s[ch] != s[ch-1] :
                count +=1
        return count        
            
        