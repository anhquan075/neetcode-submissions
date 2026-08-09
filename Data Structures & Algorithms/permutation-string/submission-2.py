class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for s in s1:
            count_s1[s] = count_s1.get(s, 0) + 1

        need = len(count_s1)
        for i in range(len(s2)):
            count_s2, cur = {}, 0
            for j in range(i, len(s2)):
                count_s2[s2[j]] = 1 + count_s2.get(s2[j], 0)
                if count_s1.get(s2[j], 0) < count_s2.get(s2[j], 0):
                    break
                
                if count_s1.get(s2[j], 0) == count_s2.get(s2[j], 0):
                    cur += 1
                
                if cur == need:
                    return True
        return False