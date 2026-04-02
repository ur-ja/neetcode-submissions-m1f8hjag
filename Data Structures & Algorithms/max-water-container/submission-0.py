class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxarea = 0
        while l < r:
            length = min(heights[l], heights[r])
            breadth = r - l
            area = length * breadth
            maxarea = max(area, maxarea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxarea
        