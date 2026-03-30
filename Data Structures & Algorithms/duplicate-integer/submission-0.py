class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = {}
        for num in nums:
            if num in duplicate_map:
                return True
            else:
                duplicate_map[num] = 1

        return False