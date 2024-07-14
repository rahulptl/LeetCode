class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        prefix = [1]
        suffix = [1]
        output = []

        for i in range(0,len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        print(prefix)
        for i in range(len(nums)-1,0,-1):
            suffix.append(suffix[-1]*nums[i])
        print(suffix)
        for i in range(0,len(nums)):
            output.append(prefix[i]*suffix[len(nums)-1-i])
            print(prefix[i])
            print(suffix[len(nums)-1-i])

        return output
