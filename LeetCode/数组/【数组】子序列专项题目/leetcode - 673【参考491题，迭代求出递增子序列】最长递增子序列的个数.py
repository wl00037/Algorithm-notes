#   673.最长递增子序列的个数
#   给定一个未排序的整数数组，找到最长递增子序列的个数。

#   示例 1:
#   输入: [1,3,5,4,7]
#   输出: 2
#   解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

#   输入: [2,2,2,2,2]
#   输出: 5
#   解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。


class Solution(object):
    def findNumberOfLIS(self, nums):
        res = set()
        res.add(())
        #   不同491题的区别是：需要专门一个变量记录最长的上升子序列，以及对应的子序列内容
        max_len = float("-inf")
        result = []

        for num in nums:
            for tmp in res.copy():
                if len(tmp) == 0 or tmp[-1]<=num:
                    curr = tmp + (num,)
                    res.add(curr)
                    if len(curr) > max_len:
                        max_len = len(curr)
                        result = []
                        result.append(curr)
                    elif len(curr) == max_len:
                        result.append(curr)
                    else:
                        continue
        return max_len,result







l = [4, 6, 7, 7]
l2 = [2,2,2,2,2]
max_len,result = Solution().findNumberOfLIS(l)
print(max_len,result)