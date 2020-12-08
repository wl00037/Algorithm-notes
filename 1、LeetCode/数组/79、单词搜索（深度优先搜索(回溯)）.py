#   79.单词搜索
#   给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#   单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

#   示例：
#   输入: board = [ ['A','B','C','E'],['S','F','C','S'],['A','D','E','E'] ]
#   给定 word = "ABCCED", 返回 true
#   给定 word = "SEE", 返回 true
#   给定 word = "ABCB", 返回 false

class Solution(object):

    def exist(self, board, word):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]                         #   上下左右四个方向的扩展搜索时使用
        def check(i, j, k):
            #   (i,j)是指从board的(i,j)开始，k是指word从第k个字符开始的后缀字串；
            #   也就是说：从board[i][j]开始搜索是否能搜索到word[k:]，搜索到返回true，否则返回false；
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:                                              #   相同并且是word最后一位，直接返回True即可，说明搜索成功；
                return True

            visited.add((i, j))                                                 #   满足要求，将(i，j)加入到本次搜索路径记录内，即visited就是记录当前搜索合理的路径的；
            result = False                                                      #   声明result=False，即最终搜索失败(没有result=True)，那么最终返回False；

            for di, dj in directions:                                           #   如果不是最后一个但是和word[w]匹配，那么就需要判断它的上下左右是否和k+1匹配了；
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):                            #   如果此处没有result=True，那么33行返回的就是false
                            result = True
                            break

            visited.remove((i, j))                                              #   返回上一层，无论result=True还是False，都要将本层的路径删除，因为万一是False，上一层还要向另外的方向进行搜索，防止另外的方向搜索路径中需要这个(i，j)
            return result                                                       #   check逐层向上return的地方，如果下层返回的不是true，那么再29就不会赋值，那么此处就成为return False

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):                                              #   从(i,j)=(0,0),k=0开始逐层递归
                    return True                                                 #   递归到最后返回的还是True，说明搜索到了，最终返回True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
result = Solution().exist(board,word)
print(result)

