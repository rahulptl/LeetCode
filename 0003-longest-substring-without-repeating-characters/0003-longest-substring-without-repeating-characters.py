class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        longest_substr = 0

        sp = 0
        fp = 0
        mapping = {}
        #print(len(s))
        while(fp<len(s)):
            if s[fp] in mapping.keys() and mapping[s[fp]]>=sp:       
                sp = mapping[s[fp]]+1                
            else:
                longest_substr = max(longest_substr, (fp-sp)+1)
            #print(f"{sp=} {fp=} {mapping=} {longest_substr}")
            mapping[s[fp]] = fp    
            fp+=1

        return longest_substr

