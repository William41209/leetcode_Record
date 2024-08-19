class Solution(object):
    def times(self,t):
        comb = 1
        for i in range(1,t+1):
            comb = comb*i
        return comb
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        # n 奇數檢查
        if (n % 2 != 0):
            half_n = int((n+1)/2)
            if (n == 1):
                return 1
        else:
            half_n = int(n/2)
        for i in range(0,half_n+1):
            sum += self.times(n-i)/(self.times(i)*self.times(n-i-i))
        return sum

x = 20

sr = Solution().climbStairs(x)
print(sr)