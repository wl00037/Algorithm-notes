#   leetcode中该类型题目有两道：
#   1、面试题 08.07. 无重复字符串的排列组合
#   2、面试题 08.08. 有重复字符串的排列组合

#   示例：
#   给出字符串 s = "abc"，得到所有的排列情况如下：['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#   解题思路：回溯法
#   1、

def permutation(S):
    res,path = [],''
    def backtrack(S, path, res):
        print("本次传入的param为：",S,path,res)
        if S == '':
            res.append(path)
            return
        for i in range(len(S)):
            cur = S[i]
            backtrack(S[:i] + S[i + 1:], path + cur, res)
    backtrack(S, path, res)
    return res

if __name__ == "__main__":
    s = 'abc'
    #print(permutation(s))
    permutation(s)