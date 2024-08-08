class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping = {} 
        rev_mapping = {}

        if(len(s)!=len(t)):
            return False

        for i in range(len(t)):

            a=s[i]
            b=t[i]

            if a in mapping:
                if mapping.get(a)!=b:
                    return False
            else:
                if b in rev_mapping:
                    return False
                else:
                    mapping[a] = b
                    rev_mapping[b]=a

        print(mapping)
        return True