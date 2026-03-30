class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = nums
        nums.extend(temp)
        return nums