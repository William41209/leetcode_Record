# #2 Add Two Numbers

class Solution(object):
    """
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.tmp = 0 # 進位用暫存
        self.l1  = l1
        self.l2  = l2
        self.Sum_ar = []
        # 確認 l1 跟 l2 長度
        if (len(self.l1) > len(self.l2)):
            different = len(self.l1) - len(self.l2)
            for row in range(different):
                self.l2.append(0)
        else:
            different = len(self.l2) - len(self.l1)
            for row in range(different):
                self.l1.append(0)
        for i in range(len(self.l1)):
            if (self.l1[i]+self.l2[i]+self.tmp >  9): # 進位
                if (i == 0):
                    self.Sum_ar.append(self.l1[i]+self.l2[i]-10)
                else:
                    self.Sum_ar.append(self.l1[i]+self.l2[i]+self.tmp-10)
                self.tmp = 1
            else: # 沒進位
                self.Sum_ar.append(self.l1[i]+self.l2[i]+self.tmp) 
                self.tmp = 0
            if (i == (len(self.l1)-1)):
                if (self.tmp == 1):
                    self.Sum_ar.append(1)
        return self.Sum_ar

print(Solution().addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))

"""
tmp = 0 # 進位用暫存
ar1 = [9,9,9,9,9,9,9]
ar2 = [9,9,9,9]
Sum_ar = []
# 確認 ar1 跟 ar2 長度
if (len(ar1) > len(ar2)):
    different = len(ar1) - len(ar2)
    for row in range(different):
        ar2.append(0)
else:
    different = len(ar2) - len(ar1)
    for row in range(different):
        ar1.append(0)
print(ar1)
print(ar2)
for i in range(len(ar1)):
    if (ar1[i]+ar2[i]+tmp >  9): # 進位
        if (i == 0):
            Sum_ar.append(ar1[i]+ar2[i]-10)
        else:
            Sum_ar.append(ar1[i]+ar2[i]+tmp-10)
        tmp = 1
    else: # 沒進位
        Sum_ar.append(ar1[i]+ar2[i]+tmp) 
        tmp = 0
    if (i == (len(ar1)-1)):
        if (tmp == 1):
            Sum_ar.append(1)


print(Sum_ar)
"""