class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        def is_prefix(length):

            prefix = strs[0][:length]
            return all([i.startswith(prefix) for i in strs])
        
        start, end = 0, len(min(strs))

        mid = (start+end)//2

        while start<=end:
            if is_prefix(mid):
                start = mid+1
            else:
                end = mid-1
            mid = (start+end)//2

        
        return strs[0][:mid]

            



