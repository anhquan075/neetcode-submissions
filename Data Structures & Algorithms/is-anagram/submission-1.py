class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = {}
        freq_map_t = {}

        for word in s:
            if word not in freq_map_s:
                freq_map_s[word] = 1
            else:
                freq_map_s[word] += 1
        
        for word in t:
            if word not in freq_map_t:
                freq_map_t[word] = 1
            else:
                freq_map_t[word] += 1
        
        return freq_map_s == freq_map_t