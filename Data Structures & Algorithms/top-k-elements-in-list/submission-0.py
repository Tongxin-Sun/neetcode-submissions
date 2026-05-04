class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print("nums: ", nums)
        hash_map = {}
        arr = [[] for _ in range(len(nums) + 1)]
        res = []
        print(arr)
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1

        for pair in hash_map.items():
            num, count = pair
            arr[count].append(num)
        
        for i in range(len(arr)-1, -1, -1):
            while len(arr[i]) != 0:
                if k == 0:
                    return res
                res.append(arr[i].pop())  
                k -= 1
            if k == 0:
                return res