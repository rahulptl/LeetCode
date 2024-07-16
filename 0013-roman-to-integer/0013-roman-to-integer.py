class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        int_value = 0
        index = 0
        while index<len(s):
            print(index, s[index])
            if s[index] == "I":
                if (index+1)<(len(s)) and s[index+1] == "V":
                    int_value += 4
                    index+=1
                elif (index+1)<(len(s)) and s[index+1] == 'X':
                    int_value+=9
                    index+=1
                else:
                    int_value+=mapping.get(s[index]) 
            elif s[index] == 'X':
                if (index+1)<(len(s)) and s[index+1] == 'L':
                    int_value+=40
                    index+=1
                elif (index+1)<(len(s)) and s[index+1] == 'C':
                    int_value+=90
                    index+=1
                else:
                    int_value+=mapping.get(s[index])    

            elif s[index] == 'C':
                if (index+1)<(len(s)) and s[index+1] == 'D':
                    int_value+=400
                    index+=1
                elif (index+1)<(len(s)) and s[index+1] == 'M':
                    int_value+=900
                    index+=1
                else:
                    int_value+=mapping.get(s[index])    
            else:
                int_value+=mapping.get(s[index])  
            index+=1         
            print(int_value)
        return int_value
