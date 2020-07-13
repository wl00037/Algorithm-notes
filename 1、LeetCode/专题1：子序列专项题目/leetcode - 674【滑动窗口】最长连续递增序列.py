#   674.最长连续递增序列
#   给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。

#   示例 1:
#   输入: [1,3,5,4,7]
#   输出: 3
#   解释: 最长连续递增序列是 [1,3,5], 长度为3。尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

#   这种条件为连续的，基本都可以用 "滑动窗口" 的思想来解决；这道题连续子序列，其实就和子串的概念是一样的。。。。

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



l1 = [1,1,1,2,2,2,3,3,3]
l2 = [2,2,2,2,2]
max_len,result = Solution().findNumberOfLIS(l1)
print(max_len,result,len(result))