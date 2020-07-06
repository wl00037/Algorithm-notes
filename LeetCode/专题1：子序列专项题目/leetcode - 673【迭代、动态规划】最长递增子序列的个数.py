#   673.最长递增子序列的个数
#   给定一个未排序的整数数组，找到最长递增子序列的个数。

#   示例 1:
#   输入: [1,3,5,4,4,7]
#   输出: 2
#   解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 、[1, 3, 5, 7]和[1, 3, 4, 7]
#       这里需要特别注意，两个[1, 3, 4, 7] 分别是指两个4，即相同的元素算两个子序列，也就是说[1,3,4,4,7]，这个子序列是不合法的；

#   输入: [2,2,2,2,2]
#   输出: 5
#   解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#           这个示例告诉我们，一个子序列中不允许出现相同的两个元素，相同的元素算两个子序列


class Solution(object):
    #   迭代过程中判断满足条件的最长子序，该方法可以实现，但是leetcode上超时了。
    def findNumberOfLIS(self, nums):
        res = list()
        res.append([])
        max_len = float("-inf")
        result = []
        for num in nums:
            for tmp in res.copy():
                if len(tmp) == 0 or tmp[-1]<num:        #   相同元素算两个子序列，即一个子序列中不允许出现相同元素，所以不能用<=
                    curr = tmp + [num]
                    res.append(curr)
                    if len(curr) > max_len:
                        max_len = len(curr)
                        result = []
                        result.append(curr)
                    elif len(curr) == max_len:
                        result.append(curr)
                    else:
                        continue
        return max_len,result

l1 = [1,1,1,2,2,2,3,3,3]
l2 = [2,2,2,2,2]
max_len,result = Solution().findNumberOfLIS(l1)
print(max_len,result,len(result))