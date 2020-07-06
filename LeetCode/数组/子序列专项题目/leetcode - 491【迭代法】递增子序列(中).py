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
        res = set()         #   res = set(())不行，还必须得用res.add(())
        res.add(())
        for num in nums:
            for tmp in res.copy():
                #   这个地方一定要用res.copy()，否则会报错，错误如下：
                #   RuntimeError: Set changed size during iteration - 迭代器不能在迭代构成中更改值
                if len(tmp) == 0 or num >= tmp[-1]:
                    n = tmp+(num,)
                    res.add(n)
        return [result for result in res if len(result)>=2]     #   然后将所有满足上升条件的元组再过滤，只留下长度大于2的

result = Solution().findSubsequences([1,1,1,2,2,2,3,3,3])
print(len(result),result)

