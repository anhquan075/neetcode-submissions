class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(numbers):
            if target - num in mapping:
                return [mapping[target - num], i + 1]
            mapping[numbers[i]] = i + 1
            print(mapping)