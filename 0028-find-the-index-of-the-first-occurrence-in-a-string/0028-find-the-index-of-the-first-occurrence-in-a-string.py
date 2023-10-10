class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        

        needle_len = len(needle)

        lp = 0
        rp = needle_len 
        while rp<=len(haystack):
            if haystack[lp:rp]==needle:
                return lp
            else:
                lp+=1
                rp+=1
            
        return -1