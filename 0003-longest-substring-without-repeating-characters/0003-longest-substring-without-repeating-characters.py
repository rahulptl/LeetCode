class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        longest_substr = 0

        sp = 0
        fp = 0
        mapping = {}
        print(len(s))
        while(fp<len(s)):
            if s[fp] in mapping.keys():       
                pointer_to_remove_till =    mapping[s[fp]]      
                while sp<=pointer_to_remove_till:
                    #print(f"{sp=}, popping {s[sp]}")
                    mapping.pop(s[sp])
                    sp+=1
            else:
                mapping[s[fp]] = fp
                fp+=1
                longest_substr = max(longest_substr, (fp-sp))
            #print(f"{sp=} {fp=} {mapping=} {longest_substr}")


        return longest_substr

