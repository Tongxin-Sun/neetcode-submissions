"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def not_overlapping(list1, list2):
            return list1.start >= list2.end or list2.start >= list1.end
        intervals_sorted = sorted(intervals, key = lambda x: x.start)
        stack = [Interval(-1, -1)]

        
        for i in range(len(intervals_sorted)):
            if not not_overlapping(stack[-1], intervals_sorted[i]):
                return False
            stack.append(intervals_sorted[i])  

        return True  