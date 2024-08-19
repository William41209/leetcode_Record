class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        Len_nums = len(nums)
        i = 0
        while (i > -1):
            if (Len_nums == 1):
                return nums[0]
            for j in range(1,Len_nums):
                if (nums[0] == nums[j]):
                    nums.pop(j)
                    nums.pop(0)
                    break
                if (j == (Len_nums-1)):
                    return nums[0]
            Len_nums -= 2
        
a = [3,5,6,5,3]
sr = Solution().singleNumber(a)
print("唯一數：",sr)