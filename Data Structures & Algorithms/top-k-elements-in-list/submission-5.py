class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_top_k_freq = {}
        for num in nums:
            count_top_k_freq[num] = 1 + count_top_k_freq.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count_top_k_freq.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res