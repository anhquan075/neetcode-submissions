from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        res = defaultdict(list)
        for string in strs:
            alphabet_counter = [0] * 26
            for char in string:
                alphabet_counter[ord(char) - ord("a")] += 1
            
            res[tuple(alphabet_counter)].append(string)
        
        return list(res.values())
