#   594.最长和谐子序列
#   和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
#   现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

#   示例 1:
#   输入: [1,3,2,2,5,2,3,7]
#   输出: 5
#   原因: 最长的和谐数组是：[3,2,2,2,3].

#   分析：
#   任何一个数只会存在于两个情况下，x与x-1、x与x+1


class Solution(object):
    #   方法：采用字典方式，记录所有数字出现的次数，然后每次判断出现最多的子序列；
    #   巧妙运用python - dict的get方法即可，如果没有查到对应key，则返回0
    def findLHS(self, nums):
        if len(nums) == 0:
            return 0

        max_len = float("-inf")
        dict_x = {}
        for num in nums:
            dict_x[num] = dict_x.get(num, 0) + 1
            numAddition1 = dict_x[num] + dict_x.get(num + 1, 0) if dict_x.get(num + 1, 0) !=0 else 0                    #   加1和减1的结果必须是存在的，否则不要进行考虑
            numSubtraction1 = dict_x[num] + dict_x.get(num - 1, 0) if dict_x.get(num - 1, 0) !=0 else 0
            max_len = max(max_len,numAddition1,numSubtraction1)
        return max_len

l = [1,1,1,1]
max_len = Solution().findLHS(l)
print(max_len)