class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}        
        def get_closest_value(i):
            for k,v in mapping.items():
                if str(i).startswith('4') or str(i).startswith('9'):
                    main_value = int(str(int(str(i)[0])+1) + '0'*len(str(i)[1:]))
                    sub_value = int('1'+'0'*len(str(i)[1:]))
                    return f"{mapping.get(sub_value)}{mapping.get(main_value)}", i-(main_value-sub_value)
                if i-k>=0:
                    return v, (i-k)
            
        output = ""
        while num>0:
            string, num = get_closest_value(num)
            output+=string
            print(output, num)
        return output

        