class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 顛倒
        a = a[::-1]
        b = b[::-1]
        # 長度相等確認
        len_A = len(a)
        len_B = len(b)
        ANS = ''
        Blong = True
        if (len_A < len_B):
            for i in range(0,(len_B-len_A)):
                a += '0'
        elif (len_A > len_B):
            for i in range(0,(len_A-len_B)):
                b += '0'
            Blong = False
        
        # 進位與否
        tmp = 0
        # 二進位運算
        if (Blong):
            lenG = len_B
        else:
            lenG = len_A
        for k in range(0,lenG):
            value = int(a[k]) + int(b[k]) + tmp
            if (value > 1):
                if (value == 3):
                    ANS += '1'
                else:
                    ANS += '0'
                tmp = 1
                # 最終進位
                if ((tmp == 1) & (k == lenG-1)):
                    ANS += '1'
            else:
                ANS += str(value)
                tmp = 0
                
        return ANS[::-1]
        
a = '101100111'
b = '01001010'
sr = Solution().addBinary(a,b)
print('二進位總和為：',sr)