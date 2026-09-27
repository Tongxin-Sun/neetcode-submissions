class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #O(nlogn) average and worst O(n) best
        res = [intervals[0]]
        def not_overlapping(list1, list2):
            return list1[0] > list2[1] or list2[0] > list1[1]
        for i in range(1, len(intervals)):
            second_list = intervals[i]
            if not_overlapping(res[-1], second_list):
                res.append(second_list)
            else:
                first_list = res.pop()
                res.append([min(first_list[0], second_list[0]), max(first_list[1], second_list[1])])
        return res