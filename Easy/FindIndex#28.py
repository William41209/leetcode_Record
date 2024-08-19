class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ''' 偷吃步用套件
        if (haystack.find(needle) >= 0):
            return haystack.find(needle)
        else:
            return -1
        '''
        len_Hay  = len(haystack)
        len_Need = len(needle)
        count = 0
        position = 0
        while (position < (len_Hay-len_Need+1)):
            count = position
            for i in range(0,len_Need):
                if (needle[i] != haystack[count]):
                    count += 1
                    break
                if (i == (len_Need-1)):
                    return (count-i)
                count += 1
            position += 1
        return -1