from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = {}
        for i in strs:
            a = {}
            for char in i:
                a[char] = a.get(char,0)+1
            a = str(dict(sorted(a.items())))
            if a not in output:
                output[a] = [i]
            else:
                output[a].append(i)
        return output.values()