class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        def key_map(item):
            return map[item]
        
        for i in nums:
            if i in map:
                map[i] = map[i]+1
            else:
                map[i] = 1
        d_keys = list(map.keys())
        result = sorted(d_keys , key = key_map,reverse = True)
        return result[:k]

        