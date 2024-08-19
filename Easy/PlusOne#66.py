class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len_digits = len(digits)
        Sum = 0
        Sum_Array = []
        # to int
        for i in range(0,len_digits):
            Sum += digits[i]*(10**(len_digits-1-i))
        # plus one
        Sum += 1
        Sum = str(Sum)
        len_Sum = len(Sum)
        # to array
        for i in range(0,len_Sum):
            Sum_Array.append(int(Sum[i]))
        return Sum_Array


    

x = [1,9,9]
Sum = Solution().plusOne(x)
print(Sum)