class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                break

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                sum_three = sorted_nums[left] + sorted_nums[right] + sorted_nums[i]
                if sum_three > 0:
                    right -= 1
                elif sum_three < 0:
                    left += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
                    
 

        return res

