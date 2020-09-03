#   给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

#   示例：
#   输入: S = "loveleetcode", C = 'e'
#   输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#

class Solution(object):

    #方法一：两次遍历，时间复杂度：2n ->O(n)
    def shortestToChar(self, S, C):
        # 思路：
        # 如果从index=x开始后面的字符串不再有字符C，那么后面的字符距离最近的字符C最近的距离就是距离index=x的距离，即第一遍从左向右遍历的意义；
        # 如果有场景：index=x和index=y之间的字符串，那么从右向左的第二次遍历则是处理距离右侧C比左侧C更近的情况；
        prev = float('-inf')
        result = []
        for index, value in enumerate(S):
            if value == C:
                prev = index
            result.append(index - prev)     #   [inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]


        prev = float('inf')
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                prev = i
            result[i] = min(result[i], prev - i)

        return result

    # 方法二：n^n+n的方法
    class Solution(object):
        # 思路：
        # 这个思路方法容易想到，即分别计算每一个index元素和每个出现C元素位置索引相减的绝对值，最小的那个就是最短距离。
        def shortestToChar(self, S, C):
            index_index = []
            result = []
            for i in range(0, len(S)):
                if C != S[i]:
                    continue
                index_index.append(i)

            for i in range(0, len(S)):
                min_index = abs(i - index_index[0])
                for j in range(1, len(index_index)):
                    if min_index > abs(i - index_index[j]):
                        min_index = abs(i - index_index[j])
                result.append(min_index)

            return result


S = "loveleetcodeaaaa"
C = 'e'
result = Solution().shortestToChar(S,C)
print(result)