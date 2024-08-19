# 回文題
# Palindrome Number
# 121 = True , 123 = False  , -121 = False
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #  負數直接排除
        if (x < 0):
            return False
        else:
            x = str(x)
            len_x = len(x)
            Position = len_x // 2
            count = 0
            for j in range(0,Position):
                if (x[j] != x[len_x-1-j]):
                    return False
                count += 1
            if (count == Position):
                return True

Input_Number = 12322
#Sol = Solution(Input_Number)
#Sol.PalindromeNum()       
Solution().isPalindrome(Input_Number) 


'''
Input_Number = -12321
String = str(Input_Number)

count = 0
#  負數直接排除
if (Input_Number < 0):
    print("False")
else:
    Position = len(String) // 2
    for j in range(0,Position):
        if (String[j] != String[int(len(String))-1-j]):
            print("False")
            break
        count += 1
    if (count == Position):
        print("True")
'''
