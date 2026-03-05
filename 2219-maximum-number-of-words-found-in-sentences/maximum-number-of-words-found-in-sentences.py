class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
       # for sentence in sentences:
           # words= sentence.split()
          #  count =len(words)
           # max_count = max(max_count, count)
        #return max_count    

        return max(sentence.count(" ")+ 1 for sentence in sentences )    
        