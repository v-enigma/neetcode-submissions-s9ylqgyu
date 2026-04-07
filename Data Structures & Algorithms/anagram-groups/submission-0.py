class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict ={}
        result = []
        for str in strs:
            key = tuple(sorted(str))
            if key not in group_dict:
                group_dict[key] = [str]
            else:
                group_dict[key].append(str)
        for item in group_dict:
            result.append(group_dict[item])
        return result




        