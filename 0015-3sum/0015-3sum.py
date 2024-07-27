class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        result = set()
        for index, i in enumerate(nums):
            if index<len(nums)-1:
                sp = index+1
                fp = len(nums)-1
                while sp<fp:
                    if (i+nums[sp]+nums[fp]) == 0:
                        result.add((i, nums[sp], nums[fp]))
                        sp+=1
                        fp-=1
                    elif (i+nums[sp]+nums[fp]) < 0:
                        sp+=1
                    else:
                        fp-=1
            #print(result)
        return list(result)



        return out
