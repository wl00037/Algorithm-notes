#   给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#   换句话说，第一个字符串的排列之一是第二个字符串的子串。

#   示例1: 
#   输入: s1 = "ab" s2 = "eidbaooo"
#   输出: True       --> 解释: s2 包含 s1 的排列之一 ("ba").

#   示例2: 
#   输入: s1= "ab" s2 = "eidboaoo"
#   输出: False       --> 解释: boa 不算是子串了，而是一个具有s1不同排列的子序列

#   该题目其实和“76-最小覆盖子串”比较类似，也就是说一个子串中包含了s1的所有字符串，所谓的“排列”其实就是不在乎顺序，有就行，也就是说又要用到统计了

#   方法一：暴力法
#   思路很简单，筛选出长长度和s1相同的子串，并且拿到该子串所有排列情况，挨个与s1进行比较，有匹配上的即可；
#   比如：s1 = "qwe"  -> ["qwe","wqe","weq","qew","eqw","ewq"]；数组中有任意一个和s2的子串匹配上的就表示s2具有s1的排列；
#   这个方法首先要先求出这个字符串的全排列，所以其实等于做了两道算法题，全排列的问题不要犹豫，回溯法来处理，关于回溯法的公式和思路请看回溯法的相关介绍；
#   然后再用暴力法，按个比较即可；

def checkInclusion_force(s1,s2):
    path = ''
    res = []                    #   用来存s1的排列
    def backtrack(s, path):
        if len(s) == 0:
            res.append(path)
        for i in range(0, len(s)):
            backtrack(s[0:i] + s[i+1:], path + s[i])
    backtrack(s1,path)
    for i in range(0,len(s2)-len(s1)+1):
        if s2[i:i+len(s1)] in res:
            return True
    return False

#   方法二：利用字典进行统计
#   思路很简单，组合所有可出现的并且长度和s1一样的子串，利用统计来判断每个字符以及字符出现的次数是否完全一致即可
from collections import Counter
def checkInclusion_UseDict(s1,s2):
    s1_counter = Counter(s1)
    for i in range(0,len(s2)-len(s1)+1):        #   +1 注意一下
        current_str = s2[i:i+len(s1)]
        print(current_str)
        current_str_counter = Counter(current_str)
        flag = True                                         #   对于内循环遇到问题需要结束内循环但外循环还要继续的场景，大多数加个flag就可以；
        for key,count in current_str_counter.items():
            if current_str_counter.get(key) != s1_counter[key]:
                flag = False
        if flag == True:
            return True
    return False

#   方法二：滑动窗口
#   思路：
#   1、
#   2、
def checkInclusion_SlidingWindow(s1,s2):
    pass


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidxbxaoooba"
    print(checkInclusion_force(s1,s2))