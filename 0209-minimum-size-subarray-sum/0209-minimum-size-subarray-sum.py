class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_size = 999999999

        sp = 0
        fp = 0 
        current_sum = sum(nums[sp:fp+1])
        while(fp<len(nums)):
            
            if(current_sum>=target):
                min_size = min(min_size, (fp-sp+1))
                current_sum-=nums[sp]

                sp+=1
            
            else:
                fp+=1
                if(fp<len(nums)):
                    current_sum+=nums[fp]

            #print(f"{min_size=} {sp=} {fp=}")

        if min_size==999999999:
            return 0
        else :
            return min_size
        