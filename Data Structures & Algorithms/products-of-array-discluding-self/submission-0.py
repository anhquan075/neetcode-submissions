class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_map = {}
        for i in range(len(nums)):
            product_nums = nums.copy()
            product_nums.remove(nums[i])
            res = 1
            for num in product_nums:
                res *= num
            product_map[i] = res
        
        return list(product_map.values())