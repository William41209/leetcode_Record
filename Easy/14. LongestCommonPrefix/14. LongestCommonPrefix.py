class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs = len(strs)
        Output = ''
        quitKey = False
        # 確認文字最短長度
        len_dis = []
        for i in range(0,len_strs):
            len_dis.append(len(strs[i]))
        minlen = min(len_dis)
        # 長度為1 特別處理
        if (len_strs == 1):
            Output = strs[0]
        else:
            # 確認最常重複出現值
            for j in range(0,minlen):
                for k in range(0,len_strs-1):
                    if (strs[k][j] != strs[k+1][j]):
                        k = -10
                        quitKey = True
                        break
                if (k == (len_strs-2)):
                    Output += str(strs[k][j])
                if (quitKey):
                    break
        return Output
    

strs = ['dogs','dors','dos']
sr = Solution().longestCommonPrefix(strs)
print(sr)