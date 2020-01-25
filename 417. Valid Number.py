class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        # write your code here
        i = 0
        s = s.strip() + " "
        #加一位，为了cornor case
        length = len(s) - 1

        if s[i] == '+' or s[i] =='-':
            i+=1

        nDigit, nPoint = 0, 0

        while(s[i].isdigit() or s[i] == '.'):
            if(s[i].isdigit()):
                nDigit+=1
            if(s[i] == '.'):
                nPoint+=1
            #对于整数或者小数，只需count总digit数量和小数点数量，如果都满足下面的条件，就判断走到最后时跟之前的length是否相等就好了
            i+=1

        if (nDigit<=0 or nPoint>1):
            # 必须有digit，小数点不能大于1否则即 not valid
            return False

        if(s[i] == 'e'):
            i+=1
            if s[i] == '+' or s[i] == '-':
                i += 1
            if i == length:
                # "2e10" e 后边必须有数字，否则i就会和length相等，即not valid
                return False
            while i<length:
                if not s[i].isdigit():
                    #e 后边必须有且必须是数字，否则not valid
                    return False
                i+=1
        return i == length

if __name__ == '__main__':
    print(Solution().isNumber("+210"))
