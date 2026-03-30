from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = dict(Counter(nums))
        sorted_count_freq = {k: v for k, v in sorted(count_freq.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_count_freq.keys())[:k]