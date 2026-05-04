class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            char_arr = [0] * 26
            for char in str:
                index = ord(char) - ord('a')
                char_arr[index] += 1
            key = tuple(char_arr)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(str)

        return hash_map.values()
            