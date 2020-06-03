#   LeeCode - 78、子集

#   给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#   示例:
#   输入：nums = [1,2,3]
#   输出：[ [3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[] ]

class Solution(object):

    #   方法一：用迭代的方式
    #   分析：假如我们要得到：[1,2,3]
    #   1、需要得到3的子集，可以拆解成 [3] + [1,2] 之间的组合，即[1,3][2,3][1,2,3],[3]
    #   2、要获取2的子集，可以拆解成[1] + [2]直接的组合，即[1][2][1,2]
    #   所以，可以用迭代来实现拆解，从而得到本题的答案；

    def subsets_iteration(self, nums):
        res = [[]]  #   子集也包括空集，所以要加上
        for i in range(0,len(nums)):
            current_res_len = len(res)
            for j in range(0,current_res_len):      #   利用了list有序的特点，可以每次只拿当前长度的范围做循环
                res.append([nums[i]]+res[j])
        return res


    #   方法二：回溯法

    def subsets_huisu(self, nums):
        res = []
        n = len(nums)

        def backtrack(i,tmp):
            res.append(tmp)
            for j in range(0,n):
                backtrack(j+1,tmp+[nums[j]])
        backtrack(0,[])
        return  res




nums = nums = [1,2,3]
result = Solution().subsets_iteration(nums)
print(result)


