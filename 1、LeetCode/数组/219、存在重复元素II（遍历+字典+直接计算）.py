#   219. 存在重复元素II
#   给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

#   比如：
#   输入: nums = [1,2,3,1], k = 3
#   输出: true

class Solution(object):

    #   思路：
    #   先判断是否有相同的值，然后再计算索引位的差；
    #   用字典，将所有相同的值以及对应的索引位记录下来即可；

    def containsNearbyDuplicate(self, nums, k):
        dict_all = {}
        for index,value in enumerate(nums):
            dict_all[value] = dict_all.get(value,list())
            dict_all[value].append(index)
            value_len = len(dict_all[value])
            if abs(dict_all[value][value_len-1] -  dict_all[value][value_len-2]) <= k and value_len>1:
                return True
            continue
        return False

l = [1,2,3,1]
result = Solution().containsNearbyDuplicate(l,3)
print(result)
