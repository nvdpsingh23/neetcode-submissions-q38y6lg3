class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = []
        n = len(heights)
        for i in range(n//2):
            l,r, maxi = 0, n-1,0
            while l<r:
                mod= min(heights[l],heights[r])
                length = r-l
                areas = mod*length
                maxi = max(maxi,areas)
                if l<r:
                    l+=1
                else:
                    r-=1
        return maxi
