class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        N = len(heights)
        right = N - 1

        result = 0
        while (left < right):
            W = right - left
            H = min(heights[left], heights[right])

            V = W * H

            result = max(result, V)

            if (heights[right] < heights[left]):
                right -= 1
            else:
                left += 1
        
        return result