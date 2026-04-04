class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []
        def backtrack(start):
            #basecase
            if start == len(s):
                result.append(temp[:])
                return
            #try all substring
            for end in range(start,len(s)):
                substring = s[start:end+1]

                #check pal
                if substring == substring[::-1]:
                    temp.append(substring)
                    backtrack(end+1)
                    temp.pop()
        backtrack(0)
        return result            



        