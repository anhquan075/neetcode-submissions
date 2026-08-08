class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count_freq[num] = count_freq.get(num, 0) + 1

        for num, cnt in count_freq.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res