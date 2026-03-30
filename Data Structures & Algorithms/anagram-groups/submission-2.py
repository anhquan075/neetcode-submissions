from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count_lst = [0] * 26
            for c in s:
                count_lst[ord(c) - ord("a")] += 1
            res[tuple(count_lst)].append(s)

        return list(res.values())

        