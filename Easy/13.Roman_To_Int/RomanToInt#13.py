class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        len_s = len(s)
        for i in range(0,len_s):
            # I 在 V 或 X 之前 要扣
            if (s[i] == 'I'):
                sum += 1
                if (i != (len_s - 1)):
                    if ((s[i+1] == 'V') | (s[i+1] == 'X')):
                        sum -= 2            
            elif (s[i] == 'V'):
                sum += 5
            # X 在 L 或 C 之前 要扣
            elif (s[i] == 'X'):
                sum += 10
                if (i != (len_s - 1)):
                    if ((s[i+1] == 'L') | (s[i+1] == 'C')):
                        sum -= 20
                
            elif (s[i] == 'L'):
                sum += 50
            # C 在 D 或 M 之前 要扣
            elif (s[i] == 'C'):
                sum += 100
                if (i != (len_s - 1)):
                    if ((s[i+1] == 'D') | (s[i+1] == 'M')):
                        sum -= 200
                        
            elif (s[i] == 'D'):
                sum += 500
            elif (s[i] == 'M'):
                sum += 1000
        return sum
    
s = 'MCMXCIV'
Intre = Solution().romanToInt(s)
print(Intre)