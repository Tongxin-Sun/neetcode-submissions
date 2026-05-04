class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encodedString = ""
        
        for s in strs:
            encodedString += str(len(s)) + ","
        
        encodedString += "#"

        for s in strs:
            encodedString += s
        
        return encodedString
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decodedList = []
        p1, p2 = 0, 0
        while s[p2] != "#":
            p2 += 1
        p2 += 1
        while s[p1] != "#":
            length = 0
            while s[p1] != ",":
                print(s[p1])
                length = length * 10 + int(s[p1])
                p1 += 1
            p1 += 1
            string = ""
            for i in range(length):
                string += s[p2]
                p2 += 1
            decodedList.append(string)
        return decodedList