class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict_count = {}
        majority_count = len(nums)/2
        print(majority_count)
        for i in nums:
            current_count = dict_count.get(i,0)
            new_count = current_count+1
            if new_count > majority_count:
                return i
            dict_count[i] = current_count+1

        print(dict_count)