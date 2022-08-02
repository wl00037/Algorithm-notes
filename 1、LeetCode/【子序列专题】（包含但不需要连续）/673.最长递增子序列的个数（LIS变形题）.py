
# 673.最长递增子序列的个数
# 给定一个未排序的整数数组，找到最长递增子序列的个数。

# 示例 1:
# 输入：[1,3,5,4,4,7]
# 输出：3
# 解释：有三个最长递增子序列，分别是 [1, 3, 4, 7] 、[1, 3, 5, 7]和[1, 3, 4, 7]

# 输入：[2,2,2,2,2]
# 输出：5
# 解释：最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 这个示例告诉我们，一个子序列中不允许出现相同的两个元素，相同的元素算两个子序列

class Solution(object):

    # 方法：动态规划
    # 思路：
    # 1.dp[i]：第i个元素作为子序列的最后一个元素时，这个子序列最大上升子序列的长度
    # 2.统计dp数组中最大的一个值的数量，就是本题的答案
    def findNumberOfLIS_solution1(self, nums):

        # dp[i]：以nums[i]结尾的最长LIS的长度
        dp = [1] * len(nums)

        # counter[i]：以nums[i]结尾的最长LIS个数
        counter = [1] * len(nums)

        for index,value in enumerate(nums):

            # 再遍历一次0~i-1，目的是判断当前的nums[i]是否可以放到nums[0]~nums[i-1]这个区域内每一个元素之后，加长上升子序列的长度
            for j in range(index):

                if nums[j] < value:

                    #  dp[i]记录更长的递增子序列
                    if dp[j]+1 > dp[index]:

                        # 更新dp[i]：以nums[index]为结尾的LIS长度更新
                        dp[index] = dp[j]+1
                        # nums[index]可以直接附加在以nums[j]结尾的LIS后，并且以nums[index]元素结尾的LIS类型数量就是nums[j]为结尾的类型数量
                        counter[index] = counter[j]

                    # 如果：j遍历过程中，有"其他路径+nums[i]"和当前的dp[i]一样大（即其他路径 + nums[i]也达到了最长递增子序列长度）
                    elif dp[j]+1 == dp[index]:

                        # 那么i元素作为子序列最后一个元素时，它的所有路径情况为：
                        # 当前已知的路径类型counter[i] + 此次遍历到j时的路径类型counter[j]
                        counter[index] = counter[index] + counter[j]

        # 拿到dp中最大上升子序列的长度
        max_lis = max(dp)
  
        ans = sum([counter[i] for i in range(len(nums)) if dp[i] == max_lis])
        return ans


    def findNumberOfLIS_solution2(self, nums):
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


if __name__ == "__main__":
    l1 = [1,1,1,2,2,2,3,3,3]
    l2 = [2,2,2,2,2]
    l3 = [1,3,5,4,4,7]
    count1 = Solution().findNumberOfLIS_solution1(l3)
    print(count1)
