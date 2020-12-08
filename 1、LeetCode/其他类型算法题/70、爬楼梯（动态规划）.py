#   假设你正在爬楼梯。需要n阶你才能到达楼顶。
#   每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？
#   注意：给定n是一个正整数。

class Solution(object):
    #   方法：动态规划
    #   思路：
    #   1、假设最后一步就到达第n阶，那么根据题目要求，只能有两种情况走这最后一步：
    #       从n-1走1步到n；
    #       从n-2走2步到n；
    #   2、所以求到n的方法就变成了：到n-1和n-2方法的和，以此类推；
    #   最后发现就是个斐波那契数列；
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        if n==2:return 2
        if n==0:return 0

        #   base case
        dp_table = [0]*n
        dp_table[0] = 1
        dp_table[1] = 2
        #   求解
        for i in range(2,n):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]
        return dp_table[n-1]

result = Solution().climbStairs(3)
print(result)