#   491. 递增子序列
#   给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#   输入: [4, 6, 7, 7]
#   输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

class Solution(object):

    #   方法一：和78题的迭代法思路非常相似，但是本题还要额外有一些条件：
    #   1、所有子集要满足上升；
    #   2、子集长度要>1，最小长度为2；
    #   3、要把相同的结果过滤掉；
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        res.add(())
        for num in nums:
            for tmp in res:
                if not tmp or num >=tmp[-1]:
                    res.add(tmp+(num,))
        return res

result = Solution().findSubsequences([4, 6, 7, 7])
print(result)

