# #1 Two Sum

class Solution(object):
    """
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target
        self.Ans_nums = [0,0]
        self.Ans_Position = []
    """
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        self.Ans_nums = [0,0]
        self.Ans_Position = []
        for i in range(len(self.nums)-1):
            self.Ans_nums[0] = self.nums[i]
            for j in range((i+1),len(self.nums)):
                if (self.target - self.Ans_nums[0] == self.nums[j]):
                    self.Ans_nums[1] = self.nums[j]
                    self.Ans_Position.append(i)
                    self.Ans_Position.append(j)
            if (self.Ans_nums[1] != 0):
                break
        return self.Ans_Position


Solution().twoSum([2,7,11,15],9)

"""
a = [2,7,11,15]
target = 9
Ans_a = [0,0]
Ans_Position = []
for i in range(len(a)-1):
    Ans_a[0] = a[i]
    for j in range((i+1),len(a)):
        if (target - Ans_a[0] == a[j]):
            Ans_a[1] = a[j]
            Ans_Position.append(i)
            Ans_Position.append(j)
    if (Ans_a[1] != 0):
        break

print(Ans_a)
print(Ans_Position)
"""