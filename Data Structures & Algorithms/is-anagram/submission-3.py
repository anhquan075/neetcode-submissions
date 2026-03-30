class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}
        for s_w, t_w in zip(s, t):
            count_s[s_w] = 1 + count_s.get(s_w, 0)
            count_t[t_w] = 1 + count_t.get(t_w, 0)

        return count_s == count_t