class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area=0
        l=0
        R= n-1
        while l< R:
            w= R-l
            h=min(heights[l],heights[R])
            a= w * h
            max_area=max(max_area, a)
            if heights[l]<heights[R]:
                l+=1
            else:
                R-=1
        return max_area
        