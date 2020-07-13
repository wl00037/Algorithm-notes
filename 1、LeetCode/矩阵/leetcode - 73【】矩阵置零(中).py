#   给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为0
#   要求：使用原地算法。

#   示例: 
#   输入：[ [1,1,1],[1,0,1],[1,1,1] ]
#   输出：[ [1,0,1],[0,0,0],[1,0,1] ]



class Solution(object):

    #   思路：方法一 - 暴力法
    #   遍历一遍，记录所有有0的行和列，然后替换就行
    #   但是估计过慢，leetcode肯定超时
    #       ⭐   本以为这个方法很low，结果超过了百分之90的执行时间。。。。。

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []

        row_length = len(matrix)
        col_length = len(matrix[0])

        for i in range(0,row_length):
            for j in range(0,col_length):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        row = set(row)
        col = set(col)                                  #   这个是为了去重，保证少进行遍历
        while len(row) != 0:
                matrix[row.pop()] = [0]*col_length      #   所有有0的行都变成0
        while len(col) != 0:                            #   把每行为0的列都进行处理
            cur = col.pop()
            for i in range(0,row_length):
                matrix[i][cur] = 0
        return matrix







matrix = [ [1,1,1],[1,0,1],[1,1,1] ]
result = Solution().setZeroes(matrix)
print(result)
