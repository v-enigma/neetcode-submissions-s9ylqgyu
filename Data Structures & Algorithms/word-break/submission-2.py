class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        wordSet = set(wordDict)

        def matchWords( index:int) -> bool:
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            for end in range(index+1, len(s)+1):
                if s[index: end] in wordSet and matchWords(end):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return matchWords(0)


               





        

        
        

        