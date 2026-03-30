from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ana_dict = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            group_ana_dict[sorted_string].append(string)

        return list(group_ana_dict.values())

        