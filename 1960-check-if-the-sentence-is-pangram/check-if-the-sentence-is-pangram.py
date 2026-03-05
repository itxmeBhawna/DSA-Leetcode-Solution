class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq ={}
        for ch in sentence:
            freq[ch] = freq.get(ch,0)+1
        return len(freq) == 26    
        