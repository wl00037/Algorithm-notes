#   leetcode中该类型题目有两道：
#   1、面试题 08.07. 无重复字符串的排列组合
#   2、面试题 08.08. 有重复字符串的排列组合

#   示例：
#   给出字符串 s = "abc"，得到所有的排列情况如下：['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#   解题思路：回溯法
#   1、

def permutation(S):
    res,path = [],''        #   res是全局变量，用来保存每一个全路径；path则表示每次的全路径的值
    def backtrack(S, path, res):        #   从当前的S中
        if S == '':             #   结束条件，可以将全路径放到res中了
            res.append(path)
            return
        for i in range(len(S)):
            cur = S[i]
            backtrack(S[:i] + S[i + 1:], path + cur, res)
            #   S[:i] + S[i + 1:] -> 刨除 S[i] 后的所有字符
    backtrack(S, path, res)
    return res

if __name__ == "__main__":
    s = 'aac'
    #print(permutation(s))
    permutation(s)