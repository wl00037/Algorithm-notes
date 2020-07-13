#   给定两个数组，编写一个函数来计算它们的交集。
#   与350题的区别就是：不展示多个重复的元素

#   示例：
#   输入: nums1 = [1,2,2,1], nums2 = [2,2]
#   输出: [2]
#

class Solution(object):
    #   方法一：暴力法
    #   思路：双层for循环，遇到相同的就删除从nums1和nums2中删除，并添加到res中；
    def intersect_Violence(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    del nums2[j]
                    break
            continue
        return list(set(res))

    #   方法二：采用空间换时间的方式，时间复杂度变为O(n)
    #   思路：分别记录nums1和nums2中元素出现的次数，然后相同key并且出现次数的差就是公共部分
    def intersect_ByDict(self, nums1, nums2):
        dict1,res = {},set()
        for i in range(len(nums1)):
            dict1[nums1[i]] = dict1.get(nums1[i],0)+1
        for j in range(len(nums2)):
            if dict1.get(nums2[j],-1) != -1:
                res.add(nums2[j])
        return list(res)





nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = Solution().intersect_ByDict(nums1,nums2)
print(result)
