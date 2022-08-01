
#   子序列：包含，但是不需要连续。比如[1,5,9,6,2]，子序列可以是[1,2]，也可以是[5,6,2]
#   子数组：包含且连续。比如[1,5,9,6,2]，子数组可以是[5,9,6]。

#   题目：最长上升子序列
#   题目分析：给定一个无序的整数数组，找到其中最长上升子序列的长度。
#   比如：[10,9,2,5,3,7,101,18]
#   输出：4 -> [2,5,7,101]

import itertools

class Solution(object):

    # 暴力法 - 时间复杂度 O(n^2)
    # 找到所有的子序列，并且判断是否为上升子序列，是的话记录下长度，并最终返回所有长度中的最大值
    def Solution_1(self , array):

        all_son_lists = []

        # 可以通过itertools.combinations来拿到所有子序列
        for i in range(1,len(array)+1):
            # append：将整个tmp作为一个元素放到all_son_lists中
            # extend：将tmp中的每一个元素分别放到all_son_lists中
            all_son_lists.extend([list(tmp) for tmp in itertools.combinations(array,i)])

        result , flag = 0 , 1
        
        # 下一步是判断是否该子序列是上升子序列
        for tmp_list in all_son_lists:

            # enumerate返回的第一个值是索引位，第二个值是索引位上的值
            for index,value in enumerate(tmp_list[:-1]):    # 这里之所以用[:-1]，目的就是下行代码中index+1不会越界

                # 判断前一个是否比后一个大，如果前一个比后一个大，则不满足上升的要求，这个子序列就是个无效的，flag置为0
                if tmp_list[index] > tmp_list[index+1]:
                    flag = 0
                    continue

            # 当这个tmp_list是一个上升序列，则需要判断，它和当前result的值谁大，当前的大则保存到result
            if flag:
                result = max(result,len(tmp_list))

            # 如果不是一个上升序列，则需要恢复flag默认值
            flag = 1

        return result



    # 动态规划方法 - 时间复杂度 O(n^2)
    def Solution_2(self , array):

        # dp数组每个index存放的都是array前index个元素中最长的上升子序列的长度
        dp = [1] * len(array)

        # 针对array为空的防御性处理
        if len(array) == 0 :
            return 0

        # 外层for循环，是为了获取array[i]的值
        for i in range(len(array)):
            # 内层for循环，是为了获取array[0] ~ array[i-1]的值
            for j in range(i):
                # 将array[i]的值分别与array[0] ~ array[i-1]的值比较
                # 如果array[i]>array[j(0~i-1)]，那么就说明array[i]满足array[j]作为上升子序列的要求
                # 也就是说dp[i]这路存放的array的前i个元素的最长子序列，可以是dp[j]+1 
                if array[i] > array[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        return  max(dp)



if __name__ == "__main__":
    
    array = [10,9,2,5,3,7,101,18]
    s = Solution()
    r1 = s.Solution_1(array)
    r2 = s.Solution_2(array)
    print("输入的array为：" + str(array))
    print("使用暴力法解题结果为：" + str(r1))
    print("使用动态规划解题结果为：" + str(r2))
