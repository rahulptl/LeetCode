class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split(' ')
        if(len(pattern)!=len(s)):
            return False

        mapping = {}
        rev_mapping = {}
        for i in range(len(pattern)):
            a= pattern[i]
            b=s[i]

            if a in mapping:
                if mapping.get(a)!=b:
                    return False
            else:
                if b in rev_mapping:
                    if rev_mapping.get(b)!=a:
                        return False
                mapping[a] = b
                rev_mapping[b]=a
        return True