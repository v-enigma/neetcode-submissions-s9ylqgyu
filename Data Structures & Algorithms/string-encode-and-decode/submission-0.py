class Solution:
    def __init__(self):
        self.lengths = []
    
    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result = result + i
            self.lengths.append(len(i))
        return result


    def decode(self, s: str) -> List[str]:
        strDecoded = []
        index = 0
        for i in self.lengths:
            strDecoded.append(s[index:index+i])
            index = index+i
        return strDecoded
