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
        print(needle_len, lp, rp)
        while rp<=len(haystack):
            print(haystack[lp:rp])
            if haystack[lp:rp]==needle:
                return lp
            else:
                lp+=1
                rp+=1
            
        return -1