class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [newInterval]
        for i in intervals:
            prev = res.pop()
            if prev[1] < i[0]:
                res.append(prev)
                res.append(i)
            elif i[1] < prev[0]:
                res.append(i)
                res.append(prev)
            else:
                new = [min(i[0], prev[0]), max(i[1], prev[1])]
                res.append(new)
        return res
