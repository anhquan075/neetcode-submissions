class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_top_k_freq = {}
        for num in nums:
            count_top_k_freq[num] = 1 + count_top_k_freq.get(num, 0)

        arr = []
        for num, cnt in count_top_k_freq.items():
            arr.append([cnt, num])

        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res