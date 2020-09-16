#   LEETCODE 581 - 最短无序连续子数组
#   给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序

#   输入: [2, 6, 4, 8, 10, 9, 15]
#   输出: 5
#   解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序

class Solution(object):
    # 方法一：排序后校验匹配
    # 思路：
    # 1、直接对数组排序，然后从index=0开始一一比对，找到排序前和排序后匹配不上的元素的开始和结束，就是题目解
    def findUnsortedSubarray(self, nums):
        new_list = sorted(nums)
        start = float("-inf")
        end = float("inf")
        for i in range(0,len(nums)):
            if nums[i] == new_list[i]:
                continue
            if start == float("-inf"):
                start = i
            else:
                end = i
        result = end+1-start if end != float("inf") else 0      # 这里是需要考虑到：如果传入的nums本身就是一个有序数组
        return result

nums = [2, 6, 4, 8, 10, 9, 15]
nums2 = [1,2,3,4]
result = Solution().findUnsortedSubarray(nums2)
print(result)