class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_left = 0
        max_right = 0

        res = 0
        n = len(height)

        for i in range(n):
            max_left = max_right = height[i]
           
            for j in range(i + 1, n):
                max_right = max(max_right, height[j])

            for j in range(i):
                max_left = max(max_left, height[j])

            res += min(max_right, max_left) - height[i]

        return res