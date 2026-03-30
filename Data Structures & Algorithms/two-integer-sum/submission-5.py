class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_sum = {}
        for i, num in enumerate(nums):
            index_sum[target - num] = i

        for j, num in enumerate(nums):
            if num in index_sum and index_sum[num] != j:
                return [j, index_sum[num]]