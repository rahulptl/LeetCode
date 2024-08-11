from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for i in strs:
            string = ''.join(sorted(i))  
            res[string].append(i)    
        return res.values()