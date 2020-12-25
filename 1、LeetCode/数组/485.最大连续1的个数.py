
#   485.最大连续1的个数
#   给定一个二进制数组， 计算其中最大连续1的个数，就是找到做多有多少个1连续

#   输入: [1,1,0,1,1,1]
#   输出: 3
#   解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

class Solution(object):

    # 方法一：暴力法，就是从元素值为1的地方向后遍历end，统计最长的记录的max_count；
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        len_nums = len(nums)
        for index,value in enumerate(nums):
            if value != 1:
                continue
            end = index
            while end < len_nums and nums[end]:     # 注意判断条件先后顺序，如果nums[end]就会range of错误
                print(" index is :",index," end is :",end,)
                max_count = max_count if max_count > end-index+1 else end-index+1
                end += 1
        return max_count

    # 方法二：对方法一其实没必要两轮遍历，一次遍历其实就可以；
    def findMaxConsecutiveOnes2(self, nums):
        max_count = 0
        tmp = 0
        for index,value in enumerate(nums):
            if value != 1:
                tmp = 0
                continue
            tmp += 1
            max_count = max_count if max_count > tmp else tmp
        return max_count




l = [1,0,1,1,1]
s = Solution().findMaxConsecutiveOnes2(l)
print(s)


