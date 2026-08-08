class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        precheck = {}
        for idx, num in enumerate(nums):
            precompute = target - num
            if precompute in precheck:
                return [precheck[precompute], idx]
            precheck[num] = idx
        
        