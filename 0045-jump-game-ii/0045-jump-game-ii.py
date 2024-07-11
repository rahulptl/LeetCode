class Solution(object):
    
    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jumps = 0
        target = len(nums)-1
        farthest = 0
        current_end = 0
        for i in range(0, len(nums)-1):
            farthest = max(i+nums[i], farthest)

            if i==current_end:
                jumps+=1
                current_end = farthest
            print(f"{i=} {current_end=} {farthest=} {jumps=}")

        return jumps

            

