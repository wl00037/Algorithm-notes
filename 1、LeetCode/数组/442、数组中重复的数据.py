
#   442. 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。找到所有出现两次的元素。

#   输入: [4,3,2,7,8,2,3,1]
#   输出: [2,3]

class Solution(object):

    #   方法一：暴力法，当前元素分别和后面的元素比较，有点像冒泡；
    #   <leetcode执行超时>
    def findDuplicates(self, nums):
        result = []
        length = len(nums)
        for i in range(0,length):
            for j in range(i+1,length):
                if nums[i] != nums[j]:
                    continue
                else:
                    result.append(nums[i])
                    continue
        return list(set(result))

    #   方法二：遍历一遍，利用数组特性，建立元素与索引位的映射;
    #   如果映射位的元素为0，则将这个元素放进去；
    #   如果映射位的元素>0，则表示重复；
    #   <Leetcode通过，并且执行时间超过100%>
    def findDuplicates2(self,nums):

        new_list = [0] * (len(nums)+1)
        result = []
        for i in nums:
            if new_list[i] == 0:
                new_list[i] = i
            else:
                result.append(i)
        return result

    #   <如果不允许采用新的空间，那么方法二就不可行，题目中其实不允许>
    #   方法三：
    #       对出现过的元素在其对应的索引位上进行标记，标记方式就是为负（nums[i]的映射对应nums[i]-1）
    #       注：判断过程中要用abs(num)来取正，否则取负的话等于索引位为负，肯定不对
    def findDuplicates3(self,nums):

        result = []
        for num in nums:
            if nums[abs(num)-1] > 0 :   #   判断abs(num)-1索引位上的值是否>0，大于0表示未出现过
                nums[abs(num) - 1] *= -1
            else:                       #   小于0就表示出现过，append到result中
                result.append(abs(num))
        return result


l = [4,3,2,7,8,2,3,1]
result = Solution().findDuplicates3(l)
print(result)

