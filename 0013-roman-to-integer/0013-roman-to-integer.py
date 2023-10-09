class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        mapper = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        i=0
        while i<len(s):
            if i==len(s)-1:
                value+=mapper.get(s[i])
            else:
                print(s[i], s[i+1], mapper.get(s[i]), mapper.get(s[i+1]))
                if s[i] == 'I':
                    if s[i+1] == 'V':
                        value+=(mapper.get(s[i+1]) - mapper.get(s[i]))
                        i=i+1
                    elif s[i+1] == 'X':
                        value+=(mapper.get(s[i+1]) - mapper.get(s[i]))
                        i=i+1
                    else:
                        value+=mapper.get(s[i])

                elif s[i] == 'X':
                    if s[i+1] == 'L':
                        value+=(mapper.get(s[i+1]) - mapper.get(s[i]))
                        i=i+1
                    elif s[i+1] == 'C':
                        value+=(mapper.get(s[i+1]) - mapper.get(s[i]))
                        i=i+1
                    else:
                        value+=mapper.get(s[i])


                elif s[i] =='C':
                    if s[i+1] == 'D':
                        value+=(mapper.get(s[i+1]) - mapper.get(s[i]))
                        i=i+1
                    elif s[i+1] == 'M':
                        value+=(mapper.get(s[i+1]) - mapper.get(s[i]))
                        i=i+1
                    else:
                        value+=mapper.get(s[i])
                
                else:
                    value+=mapper.get(s[i])
            i=i+1
            print(value)
        return value

