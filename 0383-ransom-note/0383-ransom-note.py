class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomKeys = {}
        magazineKeys ={}
        for a in ransomNote:
            ransomKeys[a] = ransomKeys.get(a,0)+1
        for a in magazine:
            magazineKeys[a] = magazineKeys.get(a,0)+1

        print(ransomKeys,magazineKeys )
        for key in ransomKeys:
            if magazineKeys.get(key) < ransomKeys.get(key):
                return False

        return True