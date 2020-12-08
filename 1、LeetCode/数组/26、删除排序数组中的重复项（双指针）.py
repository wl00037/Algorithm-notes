#   LeeCode - 26、删除排序数组中的重复项

#   给定一个排序数组，你需要在<原地>删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#   不要使用额外的数组空间，你必须在原地修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
#   示例：
#   给定数组 nums = [1,1,2], 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

class Solution(object):

    #   题目要求：在原有的数组上进行，不允许出现额外的空间使用，这么来看，用快慢指针是比较合适的
    #   思路：慢指针从index=0开始，快指针从index=1开始，当s[slow] != s[fast]时，就将s[slow+1] = s[fast]，否则就fast继续向后移动

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 1

        while(fast < len(nums)):
            if nums[slow] != nums[fast]:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        return nums[0:slow+1],slow+1

nums = [0,0,1,1,1,2,2,3,3,4]
result,length = Solution().removeDuplicates(nums)
print(result,length)


