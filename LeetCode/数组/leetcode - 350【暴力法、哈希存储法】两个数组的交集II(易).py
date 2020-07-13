#   给定两个数组，编写一个函数来计算它们的交集。
#   与349题的区别就是：重复的也要展示

#   示例：
#   输入: nums1 = [1,2,2,1], nums2 = [2,2]
#   输出: [2,2]
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
        return res

    #   方法二：采用空间换时间的方式，时间复杂度变为O(n)
    #   思路：分别记录nums1和nums2中元素出现的次数，然后相同key并且出现次数的差就是公共部分
    def intersect_ByDict(self, nums1, nums2):
        dict1,dict2,res = {},{},[]
        for i in range(len(nums1)):
            dict1[nums1[i]] = dict1.get(nums1[i],0)+1
        for j in range(len(nums2)):
            dict2[nums2[j]] = dict2.get(nums2[j],0)+1
        min_dict,max_dict = (dict1,dict2) if len(dict1)<len(dict2) else (dict2,dict1)
        for key in min_dict.keys():
            if key in max_dict:
                res.extend([key]*min(max_dict[key],min_dict[key]))
        return res




nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = Solution().intersect_ByDict(nums1,nums2)
print(result)
