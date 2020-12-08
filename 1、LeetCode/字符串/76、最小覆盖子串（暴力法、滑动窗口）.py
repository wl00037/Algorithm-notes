#   给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串；
#
#   示例：
#   输入：S = "ADOBECODEBANC", T = "ABC"
#   输出："BANC"               --> 可以不连续，并且也可以顺序不一致(要求顺序一致的话就成了求子序列了)


#   方法一：暴力法：
#   思路比较简单，还是使用两个循环组合全部可能子序列，然后分别判断是否包含目标字符串T，并找到最小子串

import collections
def minWindow_force(s,t):
    min_SubString = float("inf")
    current_SubString = ""

    #   由于子序列有长度，所以要包含t，那么长度必须>=len(t)
    #   即两个循环组合的范围是：[0:len(s)+1-len(t)]  -- [len(t)-1:len(s)]
    for i in range(0,len(s)+1-len(t)):
        for j in range(i+len(t)-1,len(s)):
            current_SubString = s[i:j+1]
            if IsInclude(current_SubString,t):
                min_SubString = min_SubString if min_SubString < j+1-i else j+1-i
    return min_SubString

def IsInclude(current_SubStrig,t):      #   是否包含了子串，包含则返回True，否则就返回False
    #   用统计来判断current_SubStrig中是否包含了所有t内的字符
    t_counter_items = collections.Counter(t)
    current_SubStrig_items = collections.Counter(current_SubStrig)
    for key,count in t_counter_items.items():
        if key in current_SubStrig_items.keys() and t_counter_items[key] <= current_SubStrig_items[key]:
            continue
        else:
            return False
    return True

#   方法二：滑动窗口
#   这道题在leetcode上的难度是困难，个人感觉之所以是困难不是因为滑动窗口不好理解，而是 “如何在滑动窗口中判断是否包含了正确的字符、字符数量” 不好处理；
def minWindow_SlidingWindow(s,t):
    min_SubString = float("inf")
    current_window = ""
    current_window_dict = {}
    t_counter = collections.Counter(t)      #   统计出每个种类字符出现的数量
    formd = 0      #   formd表示：t_counter中涉及到的字符的种类数量
    left = 0
    for right in range(0,len(s)):
        #   首先要先找到第一个满足条件：“包含所有t” 的子串;
        #   ⭐ 判断是否全部包含的时候，用的思路和暴力法的IsInclue方法类似，也要用到Counter统计，只不过还要单独设定一个变量，表示已经包含了几个数量也正确的字符；
        character = s[right]
        current_window_dict[character] = current_window_dict.get(character,0) + 1   #   该字符数量增加1
        if character in t_counter.keys() and current_window_dict.get(character) == t_counter[character]:
            formd += 1      #   formd+1 表示t中的某个字符和数量都在子串中达成，当formd==len(t_counter)，表示子串完全包含了t

        if formd == len(t_counter):     #   表示当前 s[left:right+1] 已经完全包含了 t
            min_SubString = min_SubString if min_SubString<right+1-left else right+1-left
            current_window = s[left:right+1]

            while(left<=right and formd==len(t_counter)):     #   left右移，缩小框，直到不再包含t的临界，所以判断时一定要有formd==len(t_counter)条件；
                current_window_dict[s[left]] -= 1               #   current_dict中该字符出现次数对应-1
                if s[left] in t_counter and current_window_dict[s[left]] < t_counter.get(s[left]):      #   此处就已经不再满足全包含t的条件了
                    formd -= 1
                min_SubString = min_SubString if min_SubString < right+1-left else right+1-left         #   left 向右移动每次都要更新窗口内容
                left += 1
    return min_SubString

