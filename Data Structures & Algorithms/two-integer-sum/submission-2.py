class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [0, 0]

        sum_map = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sum_map and sum_map[diff] != i:
                return [i, sum_map[diff]]
