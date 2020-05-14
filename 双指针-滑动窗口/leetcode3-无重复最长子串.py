#   给定一个字符串，请你找出其中不含有重复字符的最长子串的长度

#   示例1：
#   输入："abcabcbb"
#   输出：3    -> 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

#   示例2：
#   输入："pwwkew"
#   输出：3    -> 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#                   请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。子序列可以不连续，但是不属于子串


#   方法一：暴力法
#   思路很简单，两层循环截取出所有子串类型，然后分别判断子串是否不重复，从而找到最长子串
def lengthOfLongestSubstring_force(s):
    max_SubString = float("-inf")
    current_SubString = ""
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            current_SubString = s[i:j+1]
            if not IsRepeat(current_SubString):     # 是一个不重复的字符串
                max_SubString = max_SubString if max_SubString>j+1-i else j+1-i
    return max_SubString

def IsRepeat(SubString):
    tmp = ""
    for i in range(len(SubString)):
        if SubString[i] in tmp:
            return True
        tmp = tmp+SubString[i]
    return False


#   方法二：滑动窗口
#   思路：
#   1、首先right向右滑动，先找到一个当前满足 “不重复子串” 条件的[left:right+1]区间
#   2、然后left向右移动，找到下一个不满足条件的区间，left必须<=right
#   3、重复进行1和2，直到right到len(s)-1
#   ⭐   如果s[left:right]是不重复字符串，那么在left~right之间，s[left:right]则是最长的子串
def lengthOfLongestSubstring_SlidingWindow(s):
    left,right = 0,0
    current_window = ""
    max_SubString = float("-inf")
    for right in range(0,len(s)):

        if s[right] not in current_window:      #   保证每次向后扩展后，一定是不存在于当前窗口内的字符s
            current_window = s[left:right+1]
            max_SubString = max_SubString if max_SubString > len(current_window) else len(current_window)
            current_window = current_window + s[right]
            continue

        #   当s[right]的字符已经在窗口中时，这个时候就需要left向右进行缩减窗口了，缩减到s[left] == s[right]的left+1处
        while(s[left] != s[right]):     #   只要s[left] != s[right] 就一直缩减，目的就是找到里面窗口里哪个字符和s[right]重复了
            left += 1
            current_window = s[left:right + 1]      #   随时更新缩减后的窗口内容

        left+=1     #   缩减到s[left] == s[right]的left+1处

    return max_SubString
