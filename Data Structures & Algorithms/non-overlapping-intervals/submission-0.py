class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            if current_interval[0] < last_end:
                count += 1
            else:    
                last_end = current_interval[1]
        return count