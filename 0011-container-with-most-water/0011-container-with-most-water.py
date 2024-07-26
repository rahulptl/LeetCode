class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lp = 0
        rp = len(height)-1

        max_vol = 0
        while(lp<rp):

            max_vol = max(max_vol, (min(height[rp],height[lp]))*(rp-lp))
            if height[lp] <= height[rp]:
                lp+=1
            elif height[lp] > height[rp]:
                rp-=1

            #print(max_vol, height[lp], height[rp])

        return max_vol