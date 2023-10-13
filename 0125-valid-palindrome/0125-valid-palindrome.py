import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        pattern = re.compile(r'[^a-z0-9]')

        # Replace all non-alphanumeric characters with an empty string.
        s = re.sub(pattern,'', s)
        if s == s[::-1]:
            return True
        else:
            return False