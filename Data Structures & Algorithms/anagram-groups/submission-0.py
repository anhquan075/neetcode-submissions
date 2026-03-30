from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        freq_anagrams = defaultdict(list)
        for i, string in enumerate(strs):
            sorted_char_list_str = ",".join(sorted(string))
            freq_anagrams[sorted_char_list_str].append(string)
                
        return list(freq_anagrams.values())