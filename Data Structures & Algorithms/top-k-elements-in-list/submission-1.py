class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = [[] for i in range(len(nums) + 1)]
        print(count)
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        for key, value in map.items():
            count[value].append(key)
        
        for i in range(len(nums), -1, -1):
            while count[i] and k > 0:
                res.append(count[i].pop())
                k -= 1
            if k == 0:
                return res