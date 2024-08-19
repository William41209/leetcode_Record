class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 替換
        for i in range(0,n):
            nums1[m+i] =  nums2[i]
        # 排序
        for i in range(m+n-1):
            for j in range(m+n-i-1):
                if (nums1[j] > nums1[j+1]):
                    nums1[j],nums1[j+1] = nums1[j+1],nums1[j]
        
        return nums1
    
a = [1,5,2,3,3,4]
m = 4
b = [8,9]
n = 2
sr = Solution().merge(a,m,b,n)
print(sr)