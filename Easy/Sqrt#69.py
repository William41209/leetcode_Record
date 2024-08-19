class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        IterSqrt = 1
        for i in range(0,100):
            IterSqrt = 0.5*(IterSqrt+x/IterSqrt)
        return int(IterSqrt)
    
x = 654648767679
Ans = Solution().mySqrt(x)
print(Ans)