class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        def is_common_prefix(prefix):
            for word in strs:
                if not word.startswith(prefix):
                    return False

            else:
                return True
        
        longest_prefix = ""

        min_word = min(strs, key=len)

        for char in range(len(min_word),0,-1):

            if is_common_prefix(min_word[:char]):
                return min_word[:char]
    
        return ""

