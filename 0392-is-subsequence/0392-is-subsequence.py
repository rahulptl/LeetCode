class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_pointer = 0
        s_pointer = 0
        while s_pointer<len(s):
            if t_pointer>=len(t):
                return False
            elif s[s_pointer] == t[t_pointer]:
                s_pointer+=1
                t_pointer+=1
            else:
                t_pointer+=1
            print(s_pointer,t_pointer)

        if s_pointer==len(s):
            return True
        else:
            return False