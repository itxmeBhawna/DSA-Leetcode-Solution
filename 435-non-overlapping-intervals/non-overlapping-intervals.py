class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        end = intervals[0][1]
        re_count =0 
        for start, finish in intervals[1:]:
            if start<end:
                re_count +=1
            else:
                end = finish
        return re_count            

        