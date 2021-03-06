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
    #   所以，可以用迭代来实现拆解，从而得到本题的答案以及处理过程；
    #   [1]
    #   [2] [2]+[1]=[2,1]
    #   [3] [3]+[1]=[3,1] [3]+[2]=[3,2] [3]+[2,1]=[3,2,1]
    #
    #   简单来说就是：每一行行号与上面所有行的数据分别相加，得到新的行的内容

    def subsets_iteration(self, nums):
        res = [[]]  #   子集也包括空集，所以要加上，并且空集可以每次与元素单一本身相加，将元素自身也加到子集内
        for i in range(0,len(nums)):
            current_res_len = len(res)
            for j in range(0,current_res_len):      #   利用了list有序的特点，可以每次只拿当前长度的范围做循环
                res.append([nums[i]]+res[j])
        return res


    #   方法二：回溯法
    #   思路：假如我们要求[1,2,3]的子集，用回溯法其实就是对解决树每个节点的遍历(区分全排列，全排列是对全部叶子节点的遍历)
    #                                           root
    #                       [1]                 [2]              [3]
    #
    #                 [1,2]     [1,3]       [2,3]

    #           [1,2,3]
    #
    #   遍历思路：
    #       1、当有1的时候，要求获取到所有包含1的子集
    #       2、当遍历2的时候， 要求获取所有包含2，但是不包含1的子集
    #       3、以此类推；
    #
    #   从这颗树种就能看到其实子集就是这棵树的所有节点，所以我们的目标其实就是遍历这棵树，然后每个节点都放到res中；
    #   难点：如何生成这棵树？
    #   其实，和全排列大体一样，和全排列唯一也是最关键的一点区别：
    #           ⭐⭐   已经选择过的，不再出现在待选则范围内即可，所以也就不再需要选择和撤销选择的过程！！      【关键点！！！】

    def subsets_huisu(self, nums):
        res = []
        n = len(nums)
        def backtrack(start,tmp):
            #   start：下一层递归，你可以进行选择的范围的开始的索引位；
            #   tmp：本层的path
            res.append(tmp)
            for i in range(start,n):        #   可选择范围就是 nums[start] - nums[n-1] ,当start==n,则是递归出口
                backtrack(i+1,tmp+[nums[i]])
            return res

        return backtrack(0,[])


nums = nums = [1,2,3]
result = Solution().subsets_huisu(nums)
print(result)


