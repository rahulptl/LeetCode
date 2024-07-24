class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ptr = 0
        found = 0
        for char in s:
            #print(f"{char=}, {ptr=}")
            while(ptr<len(t) and t[ptr]!=char ):
                #print(f"{t[ptr]=}")
                ptr+=1
            if(ptr<len(t)):
                ptr+=1
                found+=1

        if(found==len(s)):
            return True
        else:
            return False