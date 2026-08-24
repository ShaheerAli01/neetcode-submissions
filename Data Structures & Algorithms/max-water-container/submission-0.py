class Solution:
    def maxArea(self, heights: List[int]) -> int:
        aMax = 0
        l, r = 0, len(heights) - 1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = h * w
            aMax = max(aMax, a)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return aMax

        