#   编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#   每行中的整数从左到右按升序排列。
#   每行的第一个整数大于前一行的最后一个整数。

#   示例: 
#   输入:
#       matrix = [ [1,3,5,7], [10,11,16,20], [23,30,34,50] ]
#       target = 3
#   输出: true


class Solution(object):
    #   思路：
    #       1、index[0:m*n]：表示二维数组中的元素在映射的一维数组中的索引值
    #       2、row=index//n ; col = index%n
    #           ⭐ 这道题其实最复杂的就是如何 <映射二维数组到一维数组的索引位上>，其他就是普通的二分法即可

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left,right = 0 , m*n-1

        while left <= right:
            middle = (left + right) // 2
            row = middle // n
            col = middle % n
            if target > matrix[row][col]:
                left = middle+1
                #   这里注意一下，如middle走到target>或<时，就已经说明target无效，所以对应的+1和-1即可，middle本身已经不需要作为下次的判断范围内了；
            elif target < matrix[row][col]:
                right = middle-1
            else:
                return True
        return False

matrix = [ [1,3,5,7], [10,11,16,20], [23,30,34,50] ]
target = 24
a = Solution().searchMatrix(matrix,target)
print(a)
